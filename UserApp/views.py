
import re,requests
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render,redirect,get_object_or_404
from django.http import JsonResponse,HttpResponse
from django.conf import settings
import json,os,urllib.parse
from .models import Kadai,Answer,KadaiProgress,Material
from .forms import KadaiForm,AnswerForm,KadaiProgress
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.models import Group
from .forms import UserUpdateForm, PasswordChangeFormCustom

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

def help(request):
    return render(request, 'help.html') 

#------------------------------教材一覧---------------------------------------------
@login_required
def user_list_files(request):
    # uploadsディレクトリのパス
    folder_path = os.path.join(settings.MEDIA_ROOT, 'uploads')

    # フォルダ内のファイルとディレクトリを取得
    try:
        # mediaフォルダ内のファイル取得(リスト)
        files_and_dirs = os.listdir(folder_path)
        print('files_and_dirs', files_and_dirs)

        # DBから material_id と material_name を取得
        files_title_list = Material.objects.values('material_name', 'material_id')
        print(f"files_title_list: {files_title_list}")

        # ファイル名とDBの情報を結合
        files_with_urls = []
        for material in files_title_list:
            # 各material_idに対応するファイル名を作成
            file_name = f"{material['material_id']}.html"
            
            if file_name in files_and_dirs:
                # ファイルURLの作成
                file_url = os.path.join(settings.MEDIA_URL, 'uploads', urllib.parse.quote(file_name))

                files_with_urls.append((material['material_name'], file_url))

        print(f"files_with_urls: {files_with_urls}")

    except FileNotFoundError:
        # フォルダが存在しない場合のエラー
        files_and_dirs = []
        error_message = "指定されたフォルダが見つかりませんでした。"
        return render(request, 'Materials/materials_list.html', {'error_message': error_message})
    except Exception as e:
        # その他の例外が発生した場合のエラー
        files_and_dirs = []
        error_message = "エラーが発生しました。"
        return render(request, 'Materials/materials_list.html', {'error_message': error_message})

    # フォルダ内のファイルがある場合に表示
    return render(request, 'Materials/materials_list.html', {'files_with_urls': files_with_urls})
#------------------------------教材一覧---------------------------------------------


#------------------------------教材表示---------------------------------------------
@login_required
def send_material(request):
    # 教材一覧で選択した教材情報を取得
    if(request.method == 'POST'):
        
        material_title = request.POST.get('title')
        material_url = request.POST.get('url') #medhia/uploads/ファイル名
        

        try:
            directory, filename = os.path.split(material_url) #取得したurlを分割
            print(directory, filename)

        except requests.exceptions.RequestException as e:
            #例外処理
            print(f"Error fetching HTML file: {e}") #例外処理(エラーメッセージ出力)e)

        return render(request, 'Materials/material_display.html', {'title': material_title, 'filename': filename})

    return HttpResponse('Invalid request', status=400)

#------------------------------教材表示---------------------------------------------

#------------------------------埋込教材ページの展開-------------------------------------

def load_file(request, file_name):
    # ファイルのパスを取得
    file_path = str(settings.MEDIA_ROOT)+ '/uploads/'+ file_name
    print(file_path)

    try:
        with open(file_path, 'r' ,encoding='utf-8') as f:
            file_content = f.read()
        
        return HttpResponse(file_content, content_type='text/html')

    except FileNotFoundError:
        return HttpResponse('File not found', status=404)
    
#-------------------------------------------------------------------------------------




#----------------------------------------------課題一覧---------------------------------------------
@login_required
#課題一覧
def Kadai_list (request):
    current_user = request.user

    kadais_by_category = Kadai.objects.values('category').distinct()  # カテゴリごとにグループ化
    categories = {}
    for category in kadais_by_category:
        category_name = category['category']
        # 各カテゴリの課題を取得
        kadais = Kadai.objects.filter(category=category_name)

        # 課題ごとに進捗状況を取得して付加
        kadai_list = []
        for kadai in kadais:
            progress = KadaiProgress.objects.filter(user=current_user, kadai=kadai).first()
            kadai.progress = progress.progress if progress else "未着手" # type: ignore
            kadai_list.append(kadai)

        categories[category_name] = kadai_list

    return render(request, 'Kadai/kadai_list.html', {'categories': categories})

#---------------------------------------------------------------------------------------------------

#-----------------------------------------課題表示---------------------------------------------

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

@csrf_exempt
def check_code(request):
    print('start1')

    if request.method != 'POST':
        return JsonResponse({"error": "POSTメソッドで送信してください"}, status=400)

    try:
        data = json.loads(request.body)
        submitted_code = data.get('code')
        kadai_id = data.get('kadai_id')

        print(f'問題番号: {kadai_id}')
        print(f'ユーザーコード: {submitted_code}')

        # 該当する課題を取得
        kadai = get_object_or_404(Kadai, number=kadai_id)
        test_case = Answer.objects.filter(kadai=kadai).first()

        if not test_case:
            return JsonResponse({"error": "該当するテストコードが見つかりません"}, status=404)

        test_code = test_case.a_text
        print(f'テストコード: {test_code}')

        #user_script_path = 'C:\\Users\\210011\\AppData\\Local\\Temp\\tmpvgor2261.py'
        #test_script_path = 'C:\\Users\\210011\\AppData\\Local\\Temp\\tmpsabkhcux.py'

        user_script_path = None
        test_script_path = None

        try:
            # ユーザーコードを一時ファイルに保存
            with tempfile.NamedTemporaryFile(delete=False, suffix=".py") as user_script:
                user_script.write(submitted_code.encode('utf-8'))
                user_script_path = user_script.name
                print(f'ユーザーコードを保存: {user_script_path}')

            # テストコードを一時ファイルに保存
            with tempfile.NamedTemporaryFile(delete=False, suffix=".py") as test_script:
                test_script.write(test_code.encode('utf-8'))
                test_script_path = test_script.name
                print(f'テストコードを保存: {test_script_path}')

            # ユーザーコードを実行するために、テストスクリプトと一緒に実行
            result = subprocess.run(
                ["python", test_script_path, user_script_path], 
                capture_output=True, text=True, timeout=10
            )

            print(f"stdout: {result.stdout}")
            print(f"stderr: {result.stderr}")
            print(f"returncode: {result.returncode}")

            # 結果が期待通りか判定
            is_correct = result.returncode == 0
            
            # 課題進行状況の更新
            user = request.user
            progress, _ = KadaiProgress.objects.get_or_create(user=user, kadai=kadai)
            progress.progress = '完了' if is_correct else '実行中'
            progress.save()

            return JsonResponse({"isCorrect": is_correct, "output": result.stdout})

        except subprocess.TimeoutExpired:
            return JsonResponse({"error": "テストの実行がタイムアウトしました"}, status=500)
        except Exception as e:
            return JsonResponse({"error": f"テストの実行に失敗しました: {e}"}, status=500)
        finally:
            if user_script_path and os.path.exists(user_script_path):
                os.remove(user_script_path)
            if test_script_path and os.path.exists(test_script_path):
                os.remove(test_script_path)

    except json.JSONDecodeError:
        return JsonResponse({"error": "無効なJSONデータです"}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

'''
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
            correct_answer = Answer.objects.filter(kadai=kadai)
            
            if not correct_answer.exists():
                print('end - 該当する解答が見つかりません')
                return JsonResponse({"error": "該当する解答が見つかりません"}, status=404)
            is_correct = any(
                submitted_code.splitlines() == answer.a_text.splitlines() for answer in correct_answer
            )
            
            # 提出されたコードと正解コードの比較
            if is_correct:
                print('end3 - 正解')
                try:
                    user = request.user
                    progress, created = KadaiProgress.objects.get_or_create(user=user, kadai=kadai)
                    progress.progress = '完了'
                    progress.save()
                    print(f'進捗状況を更新: {user.username} - 課題 {kadai.number} - 完了')
                except Exception as e:
                    print(f'進捗更新エラー: {e}')
                    return JsonResponse({"error": "進捗状況の更新に失敗しました"}, status=500)

                return JsonResponse({"isCorrect": True})
            else:
                
                print('end4 - 不正解')
                try:
                    user = request.user
                    progress, created = KadaiProgress.objects.get_or_create(user=user, kadai=kadai)
                    progress.progress = '実行中'
                    progress.save()
                    print(f'進捗状況を更新: {user.username} - 課題 {kadai.number} - 実行中')
                except Exception as e:
                    print(f'進捗更新エラー: {e}')
                    return JsonResponse({"error": "進捗状況の更新に失敗しました"}, status=500)
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
'''
#-------------------------------------------------------------------------------------



#フリーモード
def FreeMode (request):
    return render(
        request,
        'free/Free.html',
    )

#フリーモード
def Public_FreeMode (request):
    return render(
        request,
        'free/Public_Free.html',
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



#------------------------------課題進行状況--------------------------------

@login_required
def user_progress(request):
    # ログイン中のユーザーを取得
    current_user = request.user
    
    # ユーザーに紐付いた課題進捗データを取得
    progress_data = KadaiProgress.objects.filter(user=current_user).select_related('kadai')

    return render(request, 'Progress/progress.html', {'progress_data': progress_data})

#------------------------------課題進行状況--------------------------------








# #ユーザー情報変更画面（一般ユーザー用）
@login_required
def user_info(request):
    #ユーザーがuserグループに所属しているか確認
    if not request.user.groups.filter(name='user').exists():
        messages.error(request, "このページにアクセスする権限がありません")
        return redirect('home') #適切なページにリダイレクト
    
    if request.method == 'POST':
        #ユーザー名を更新するフォームを処理
        user_form = UserUpdateForm(request.POST, instance=request.user)
        password_form = PasswordChangeFormCustom(user=request.user, data=request.POST)

        #ユーザー名変更の処理
        if 'update_user' in request.POST and user_form.is_valid():
            user_form.save()
            messages.success(request, "ユーザー名が更新されました。")
            return redirect('UserApp:user_info')    #更新後にリダイレクト
        
        #パスワード変更の処理
        elif 'update_password' in request.POST and password_form.is_valid():
            password_form.save()
            update_session_auth_hash(request, request.user) #パスワード変更後にセッションを更新
            messages.success(request, "パスワードが更新されました。")
            return redirect('UserApp:user_info')    #更新後にリダイレクト
        
    else:
        #GETリクエストの際はフォームを表示
        user_form = UserUpdateForm(instance=request.user)
        password_form = PasswordChangeFormCustom(user=request.user)

    return render(request, 'registation/user_info.html', {
        'user_form': user_form,
        'password_form': password_form,
    })


#------------------------------課題進行状況--------------------------------

