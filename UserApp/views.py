
import re
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render,redirect,get_object_or_404
from django.http import JsonResponse
from django.conf import settings
import json,os,urllib.parse
from .models import Kadai,Answer
from .forms import KadaiForm,AnswerForm
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

    return render(request, 'Kadai/list.html', {'categories': categories})


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


#--------------------------教材一覧リスト--------------------------------

def list_files(request):
    # uploadsディレクトリのパス
    folder_path = os.path.join(settings.MEDIA_ROOT, 'uploads')

    # フォルダ内のファイルとディレクトリを取得
    try:
        files_and_dirs = os.listdir(folder_path)
    except FileNotFoundError:
        # フォルダが存在しない場合のエラーハンドリング
        files_and_dirs = []
        error_message = "指定されたフォルダが見つかりませんでした。"
        return render(request, '.html', {'error_message': error_message})

    # ファイルのURLを作成 (エンコード処理を追加)
    file_urls = [
        os.path.join(settings.MEDIA_URL, 'uploads', urllib.parse.quote(file)) 
        for file in files_and_dirs
    ]
    # ファイル名とURLを組み合わせたタプルのリストを作成
    files_with_urls = zip(files_and_dirs, file_urls)

    # フォルダ内のファイルがある場合に表示
    return render(request, 'list_files.html', {'files_with_urls': files_with_urls})


#-----------------------------------------------------------------------
