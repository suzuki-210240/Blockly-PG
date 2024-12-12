
import re,requests
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render,redirect,get_object_or_404
from django.http import JsonResponse,HttpResponse
from django.conf import settings
import json,os,urllib.parse
from .models import Kadai,Answer,Material,KadaiProgress
from .forms import KadaiForm,AnswerForm,KadaiProgress
from django.contrib.auth.decorators import login_required

@login_required
def Home (request):

    context = {}    #ユーザー名と権限名の入れ物
    #↓ログインされていればユーザー名と権限名取得
    if request.user.is_authenticated:
        user = request.user
        group_names = [group.name for group in user.groups.all()]

        if 'admin' in group_names:
            group_display = "管理者"
        elif 'user' in group_names:
            group_display = "一般ユーザー"
        else:
            group_display = "未分類"
        
        context['user_info'] = {
            'username' : user.username,
            'group' : group_display
        }

    #↓contextと一緒にページをレンダリング
    return render(
        request,
        'home/main.html',
        context
    )

@login_required
#課題一覧
def Kadai_list (request):
    kadais_by_category = Kadai.objects.values('category').distinct()  # カテゴリごとにグループ化
    categories = {}
    for category in kadais_by_category:
        category_name = category['category']
        categories[category_name] = Kadai.objects.filter(category=category_name)

    return render(request, 'Kadai/kadai_list.html', {'categories': categories})


#------------------------------課題表示---------------------------------------------

@login_required
def Kadai_open(request, kadai_id):

    #現在のユーザーのグループを取得
    groups = request.user.groups.all()
    #グループ名に基づいて表示する内容を決定
    user_type = "一般ユーザー"  #デフォルト
    for group in groups:
        if group.name == "admin":
            user_type = "管理者"
            break

    try:
        # `kadai_id`に対応する問題を取得
        kadai = Kadai.objects.get(number=kadai_id)
        message = kadai.q_text  # 問題文
        kadai_number = kadai.number  # 問題番号
        kadai_name = kadai.name  # 問題名
    except Kadai.DoesNotExist:
        message = "指定された問題が存在しません"
        kadai_number = None
        kadai_name = None

    return render(
        request,
        'Kadai/Kadai.html',
        {
            'kadai_number': kadai_number,
            'kadai_name': kadai_name,
            'message': message,
            'user_type': user_type,
            'username': request.user.username   #ユーザー名も渡す
        }
    )

#------------------------------------------------------------------------------------


#-------------------------------正誤判定----------------------------------------------

#あらかじめ用意する解答/--複数行の文字列リテラル--/
@csrf_exempt
def check_code(request):
    print('start1')

    if request.method == 'POST':
        print('start2')
        
        try:
            # リクエストボディをJSONとしてパース
            data = json.loads(request.body)
            submitted_code = data.get('code')
            kadai_id = data.get('kadai_id')  # 送信された問題番号

            #kadai_id = kadai_id.replace(" ","") #空白を削除
            print(f'問題番号: {kadai_id}')
            
            # 問題の取得（見つからなければ404エラーを発生させる）
            
            kadai = get_object_or_404(Kadai, number=kadai_id)
            #print(f'取得した問題: {kadai.name} - {kadai.q_text}')
            
            # 解答の取得
            correct_answer = Answer.objects.get(kadai=kadai)

            print(f'解答: {submitted_code.strip()}')
            print(f'正解: {correct_answer.a_text.strip()}')

            
            # 提出されたコードと正解コードの比較
            if submitted_code.splitlines() == correct_answer.a_text.splitlines():
                print('end3 - 正解')
                return JsonResponse({"isCorrect": True})
            else:
                print('end4 - 不正解')
                return JsonResponse({"isCorrect": False})

        except json.JSONDecodeError as e:
            # JSONのデコードエラー
            print(f'JSONデコードエラー: {e}')
            return JsonResponse({"error": "無効なJSONデータです"}, status=400)

        except Kadai.DoesNotExist:
            # 問題が見つからない場合
            print(f'問題 {kadai_id} は存在しません')
            return JsonResponse({"error": f"問題 {kadai_id} は存在しません"}, status=404)

        except Answer.DoesNotExist:
            # 解答が見つからない場合
            print(f'問題 {kadai_id} に対する解答が見つかりません')
            return JsonResponse({"error": "該当する解答が存在しません"}, status=404)

        except Exception as e:
            # その他のエラー
            print(f'予期しないエラー: {e}')
            return JsonResponse({"error": str(e)}, status=500)

    # POSTメソッド以外でリクエストされた場合
    return JsonResponse({"error": "POSTメソッドで送信してください"}, status=400)

#-------------------------------------------------------------------------------------



#フリーモード
def FreeMode (request):
    return render(
        request,
        'free/Free.html',
    )


#------------------------------------------------教材一覧リスト----------------------------------------------------

def list_files(request):

    # uploadsディレクトリのパス
    folder_path = os.path.join(settings.MEDIA_ROOT, 'uploads')

    # フォルダ内のファイルとディレクトリを取得
    try:
        # mediaフォルダ内のファイル取得(リスト)
        files_and_dirs = os.listdir(folder_path)
        print('files_and_dirs', files_and_dirs)
        # dbから二次元リストとして作成[{material_name},{html_file_name}]
        db_files_name = Material.objects.values('material_name', 'html_file_name').filter(html_file_name__in=files_and_dirs)
        # db_files_nameをリストに変換
        db_files_list = list(db_files_name)
        # db_files_nameの内容を確認
        print(f"db_files_name: {db_files_list}")
        # db_files_listをhtml_file_name順に並べ替え、files_and_dirsの順番でmaterial_nameを取得
        material_dict = {material['html_file_name']: material['material_name'] for material in db_files_list}
        # files_and_dirsの順番に従って、対応するmaterial_nameを取得
        db_material_names = [material_dict[file_name] for file_name in files_and_dirs if file_name in material_dict]
        # 並び替えた結果を表示
        print(f"db_material_names: {db_material_names}")

    except FileNotFoundError:
        # フォルダが存在しない場合のエラーハンドリング
        files_and_dirs = []
        error_message = "指定されたフォルダが見つかりませんでした。"
        return render(request, 'Materials/materials_list.html', {'error_message': error_message})
    except Exception as e:
        # その他の例外が発生した場合のエラーハンドリング
        files_and_dirs = []
        error_message = "エラーが発生しました。"
        return render(request, 'Materials/materials_list.html', {'error_message': error_message})

    print('ファイルのurl作成')
    # ファイルのURLを作成 (エンコード処理を追加)
    file_urls = [
        os.path.join(settings.MEDIA_URL, 'uploads', urllib.parse.quote(file)) 
        for file in files_and_dirs
    ]
    # ファイル名とURLを組み合わせたタプルのリストを作成
    files_with_urls = zip(db_material_names, file_urls)
    # フォルダ内のファイルがある場合に表示
    return render(request, 'Materials/materials_list.html', {'files_with_urls': files_with_urls})
#-----------------------------------------------教材一覧リスト--------------------------------------------------

#----------------------------教材表示-----------------------------------
def send_material(request):

    # 教材一覧で選択した教材情報を取得
    if(request.method == 'POST'):
        material_title = request.POST.get('title')
        material_url = request.POST.get('url') #medhia/uploads\ファイル名
        print(material_title, material_url)

        try:
            # MEDIA_ROOT を基準に絶対パスを作成
            material_url = os.path.join(settings.MEDIA_URL, material_url.replace("\\", "/"))
            print(material_url)

        except requests.exceptions.RequestException as e:
            #例外処理
            print(f"Error fetching HTML file: {e}") #例外処理(エラーメッセージ出力)e)

        return render(request, 'Materials/material_display.html', {'title': material_title, 'url': material_url})

    return HttpResponse('Invalid request', status=400)
#----------------------------教材表示-----------------------------------

#------------------------------課題進行状況--------------------------------

@login_required
def user_progress(request):
    # ログイン中のユーザーを取得
    current_user = request.user
    
    # ユーザーに紐付いた課題進捗データを取得
    progress_data = KadaiProgress.objects.filter(user=current_user).select_related('kadai')

    return render(request, 'Progress/progress.html', {'progress_data': progress_data})

#------------------------------課題進行状況--------------------------------