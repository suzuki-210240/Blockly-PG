import re
from django import forms
from django.urls import reverse
import os,requests,urllib.parse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.admin.views.decorators import staff_member_required
from .models import Material, Kadai, Answer
from .forms import  KadaiForm,AnswerForm, ValidateMaterialForm,AnswerFormSet
from django.core.files.storage import default_storage
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User, Group
from .forms import UserGroupForm
from django.http import HttpResponse,Http404, JsonResponse
from django.db import transaction, IntegrityError
from django.shortcuts import render
from urllib.parse import quote


#管理者のみがアクセスできるビューのデコレーター
def is_admin(user):
    return user.groups.filter(name='admin').exists()

#管理者用のアカウント管理ページ
@login_required
@user_passes_test(is_admin)
def account_management(request):
    users = User.objects.exclude(is_superuser=True)  #すべてのユーザーを取得（スーパーユーザーを除く）
    if request.method == 'POST':
        form = UserGroupForm(request.POST)
        if form.is_valid():
            #フォームから取得したユーザーIDとグループ名を使って、ユーザーオブジェクトとグループを取得
            user = form.cleaned_data['user']  #ここでUserオブジェクトを取得
            group_name = form.cleaned_data['group'] #グループ名

            #グループオブジェクトを取得
            group = Group.objects.get(name=group_name)

            #ユーザーのグループを変更
            user.groups.clear() #現在のグループを削除
            user.groups.add(group)  #新しいグループを追加

            #更新後にリダイレクト
            return redirect('AdminApp:account_management')
    else:
        form = UserGroupForm()

    return render(request, 'admin/account_management.html', {'users': users, 'form': form})

#アカウント削除メソッド
@login_required
@user_passes_test(is_admin)
def account_management_delete(request, user_id):
    user = get_object_or_404(User, id=user_id)
    #ユーザーを削除
    user.delete()
    #削除後にアカウント管理ページにリダイレクト
    return redirect('AdminApp:account_management')



@login_required
def admin_menu(request):
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
    return render(request, 'home/admin_menu.html', context)


def admin_materials_list(request):
    return render(request, 'Materials/admin_materials_list.html')

def add_materials(request):
    return render(request, 'Materials/add_Materials.html')

def wait_page(request):
    return render(request, 'Materials/wait_page.html')

def next_page(request):
    return render(request, 'AdminApp:admin_kadai_list')

def edit_materials(request):
    # 教材一覧で選択した教材情報を取得
    if(request.method == 'POST'):
        old_title = request.POST.get('title')
        old_url = request.POST.get('url') #medhia/uploads\ファイル名
        print(old_title, old_url)
        old_url = os.path.join(settings.MEDIA_URL, old_url.replace("\\", "/"))
        print(old_url)
    return render(request, 'Materials/edit_Materials.html', {'old_title': old_title, 'old_url': old_url})


def delete_materials(request):
    # 教材一覧で選択した教材情報を取得
    if(request.method == 'POST'):
        print("start")
        material_title = request.POST.get('title')
        material_url = request.POST.get('url') #medhia/uploads\ファイル名
        print(material_title, material_url)

        try:
            directory, filename = os.path.split(material_url)
            print(directory, filename)
            folder_path = os.path.join(settings.MEDIA_URL, 'uploads/')
            print("folder_path:",folder_path)

        except requests.exceptions.RequestException as e:
            #例外処理
            print(f"Error fetching HTML file: {e}") #例外処理(エラーメッセージ出力)e)

        return render(request, 'Materials/delete_materials.html', {'title': material_title, 'filename': filename, 'url': material_url})

    return HttpResponse('Invalid request', status=400)


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
    
#-----------------------------------画面遷移----------------------------------------------


#----------------------------教材一覧リスト------------------------------------

def admin_list_files(request):
    print('admin_list_files')
    # uploadsディレクトリのパス
    folder_path = os.path.join(settings.MEDIA_ROOT, 'uploads')

    # フォルダ内のファイルとディレクトリを取得
    try:
        # mediaフォルダ内のファイル取得(リスト)
        files_and_dirs = os.listdir(folder_path)

        # DBから material_id と material_name を取得
        files_title_list = Material.objects.values('material_name', 'material_id')

        # ファイル名とDBの情報を結合
        files_with_urls = []
        for material in files_title_list:
            # 各material_idに対応するファイル名を作成
            file_name = f"{material['material_id']}.html"
            
            if file_name in files_and_dirs:
                # ファイルURLの作成
                file_url = os.path.join(settings.MEDIA_URL, 'uploads', file_name)

                files_with_urls.append((material['material_name'], file_url.replace("\\", "/")))


    except FileNotFoundError:
        # フォルダが存在しない場合のエラー
        files_and_dirs = []
        error_message = "指定されたフォルダが見つかりませんでした。"
        return render(request, 'Materials/admin_materials_list.html', {'error_message': error_message})
    except Exception as e:
        # その他の例外が発生した場合のエラー
        files_and_dirs = []
        error_message = "エラーが発生しました。"
        return render(request, 'Materials/admin_materials_list.html', {'error_message': error_message})

    # ファイルのURLを作成 (エンコード処理を追加)
    file_urls = [
        os.path.join(settings.MEDIA_URL, 'uploads', urllib.parse.quote(file)) 
        for file in files_and_dirs
    ]

    # フォルダ内のファイルがある場合に表示
    return render(request, 'Materials/admin_materials_list.html', {'files_with_urls': files_with_urls})

def download_template(request):
    # ダウンロードするファイルのパスを指定
    file_path = os.path.join(settings.BASE_DIR, 'static','admin', 'template', 'template_material.html')
    print(file_path)

    # ファイルが存在する場合、ダウンロードを開始
    if os.path.exists(file_path):
        with open(file_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type='application/octet-stream')
            response['Content-Disposition'] = f'attachment; filename={os.path.basename(file_path)}'
            return response
    else:
        # ファイルが見つからなかった場合、404エラーを返す
        return HttpResponse('File not found', status=404)

#----------------------------教材一覧リスト-----------------------------------

#--------------------------教材ファイル新規追加--------------------------------

def add_file(request):
    print('add_file')
    if request.method == 'POST':
        print("Uploaded files:", request.FILES)
        
        # バリデーションフォームインスタンス作成
        form = ValidateMaterialForm(request.POST, request.FILES)
        
        if form.is_valid():  # バリデーションが有効な場合
            # 教材タイトルの取得 
            title = form.cleaned_data['title']
            
            # アップロードされたファイルの取得
            uploaded_file = request.FILES['html_file']
            # アップロードされたファイル名の取得（元のファイル名）
            original_file_name = uploaded_file.name

            # アップロードされた画像ファイルの取得(複数)
            image_file = request.FILES.getlist(quote('img_file'))

            # トランザクションを開始
            try:
                with transaction.atomic():
                    # データベースに新しい教材を保存し、material_id を取得
                    material = Material.objects.create(
                        material_name=title,
                        html_file_name=original_file_name  # ファイル名は元の名前
                    )
                    print(material)
                    material.save()

                    # 保存した最新の教材IDを取得(DB)
                    material_id = material.material_id  # すでに作成したオブジェクトから取得
                    print('material_id', material_id)

                    # 保存先のパスを作成（ファイル名は material_id）
                    file_name_with_id = f"{material_id}.html"  # 例：ファイル名を material_id.html として保存
                    file_path = os.path.join(settings.MEDIA_ROOT, 'uploads', file_name_with_id)
                    print(file_path)

                    # ディレクトリが存在しない場合、作成
                    os.makedirs(os.path.dirname(file_path), exist_ok=True)

                    # ファイルを保存
                    with default_storage.open(file_path, 'wb+') as destination:
                        for chunk in uploaded_file.chunks():
                            destination.write(chunk)

                                # 正常終了時
                    return render(request, 'Materials/wait_page.html', {'success_message': f"{original_file_name} を追加しました。"})

            except IntegrityError:
                # 一意制約違反などのデータベースエラー処理
                error_message = 'このタイトルは既に使用されています。'
                return render(request, 'Materials/add_materials.html', {'form': form, 'error_message': error_message})

            except Exception as e:
                # 他のエラー処理
                return render(request, 'Materials/add_materials.html', {'form': form, 'error_message': str(e)})
        else:
            # フォームが無効な場合、エラーメッセージとともに再レンダリング
            print("Form errors:", form.errors)
            return render(request, 'Materials/add_materials.html', {'form': form, 'error_message': 'フォームにエラーがあります。'})
    else:
        # 初回表示時
        form = ValidateMaterialForm()
    
    return render(request, 'Materials/add_materials.html', {'form': form})

#--------------------------教材ファイル新規追加--------------------------------

#--------------------------教材ファイル編集・削除--------------------------------

#編集
def edit_item(request):
    if request.method == "POST":
        # 現在のファイル取得
        old_file = request.POST.get("old-url", "").strip()
        # material_idを抽出
        match = re.search(r'/media/uploads/(.+?)\.html', old_file)
        old_file_id = match.group(1) if match else None

        if not old_file_id:
            return HttpResponse("No valid file name found", status=400)

        # 変更したい項目を取得
        title_choice = request.POST.get("title-choice")
        file_choice = request.POST.get("file-choice")

        # material_idを使ってDBから教材を取得
        material = get_object_or_404(Material, material_id=old_file_id)
        
        if title_choice == "no" and file_choice == "no":
            # 両方を選択しない場合
            print('title-choice == no and file-choice == no')

            return render(request, 'Materials/edit_Materials.html', {'choice_error_message': 'タイトルまたはファイルを登録してください。'})
        else:
            # タイトル変更(DB)
            if title_choice == "yes":
                print('title-choice == yes')
                new_title = request.POST.get("new-title")
                print('new_title', new_title)
                material.material_name = new_title
                material.save()

            # ファイル変更(DB) & /media/uploads/フォルダ内のファイル変更
            if file_choice == "yes":
                print('file-choice == yes')
                uploaded_file = request.FILES.get("new-file")
                original_file_name = uploaded_file.name
                file_name_with_id = f"{material.material_id}.html"
                file_path = os.path.join(settings.MEDIA_ROOT, 'uploads', file_name_with_id)

                with default_storage.open(file_path, 'wb+') as destination:
                    for chunk in uploaded_file.chunks():
                        destination.write(chunk)
                # ファイル名(DB)を変更
                material.html_file_name = original_file_name
                material.save()
        
        return render(request, 'Materials/wait_page.html')

    return HttpResponse("Method not allowed", status=405)


#削除
def delete_item(request):
    
    if request.method == 'POST':
        # uploadsディレクトリのパス
        folder_path = os.path.join(settings.MEDIA_ROOT, 'uploads')
        print('folder_path:', folder_path)
        # ファイルパスの取得
        file_path = request.POST.get("url")

        # ファイルパスがNone または`/media/uploads/`で始まらない場合
        if not file_path or not file_path.startswith("/media/uploads/"):
            return JsonResponse({"error": "Invalid file path"}, status=400)
        
        match = re.search(r'/media/uploads/(.+?)\.html', file_path)
        file_id = match.group(1)
        print('file_id:', file_id)

        file_path = os.path.join(folder_path, file_id + ".html")

        # 削除処理
        try:
            if os.path.exists(file_path):
                #medhia/uploads/ファイル名.html削除
                os.remove(file_path)
                
                # 削除するDBレコードを取得
                material = get_object_or_404(Material, material_id=file_id)
                material.delete()  # レコードを削除

                return render(request, 'Materials/wait_page.html')
            else:
                return JsonResponse({'status': 'error', 'message': 'not material'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=500)
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)

#--------------------------教材ファイル編集・削除--------------------------------

#----------------------------画像リスト表示------------------------------------

def next_img_list(request):
    try:
        image_dir = os.path.join(settings.BASE_DIR, 'static', 'images')
        files_and_dirs = os.listdir(image_dir)

        files_with_urls = []
        
        # ディレクトリ内のファイルをリスト化
        for file_name in files_and_dirs:
            if os.path.isfile(os.path.join(image_dir, file_name)):
                files_with_urls.append({
                    'name': file_name,
                    'url': quote(f'/static/images/{file_name}')
                })

        print('files_with_urls', files_with_urls)
    except FileNotFoundError:
        error_message = "指定されたフォルダが見つかりませんでした。"
        return render(request, 'Materials/img_list.html', {'error_message': error_message})
    except Exception as e:
        error_message = f"エラーが発生しました: {str(e)}"
        return render(request, 'Materials/img_list.html', {'error_message': error_message})
    
    return render(request, 'Materials/img_list.html', {'files_with_urls': files_with_urls})

# ----------------------------画像リスト表示------------------------------------

#--------------------------画像追加・削除---------------------------------------

def add_img(request):
    print('add_img')
    if request.method == 'POST':

        # 複数ファイルを取得
        image_files = request.FILES.getlist('image_files')
        print('image_files:', image_files)

        # 保存先のディレクトリを指定
        image_dir = os.path.join(settings.BASE_DIR, 'static', 'images')
        print('image_dir:', image_dir)

        for image in image_files:
            image_path = os.path.join(image_dir, image.name)

            # すでにファイルが存在するか確認
            if os.path.exists(image_path):
                # ファイル名に番号を追加する処理
                base_name, ext = os.path.splitext(image.name)
                count = 1
                while os.path.exists(image_path):
                    new_name = f"{base_name}({count}){ext}"
                    image_path = os.path.join(image_dir, new_name)
                    count += 1

            try:
                # ファイル保存
                with open(image_path, 'wb+') as destination:
                    for chunk in image.chunks():
                        destination.write(chunk)
                print(f"画像 {image.name} を保存しました。")
            except Exception as e:
                # 例外が発生した場合、エラーメッセージを表示
                error_message = f"エラーが発生しました: {str(e)}"
                return render(request, 'Materials/img_list.html', {'error_message': error_message})
        
        # 保存が完了したら、次のページへリダイレクトページに飛ばす
        return redirect('AdminApp:next_img_list')
    
    # GETリクエストの場合、フォームを表示
    return render(request, 'Materials/img_list.html')


def delete_img(request):
    print('delete_img')  # デバッグ用ログ
    if request.method == 'POST':
        # POST データから `img_name` を取得
        img_name = request.POST.get('img_name')
        print('img_name:', img_name)  # デバッグ用ログ

        # img_name が None または空の場合の処理
        if not img_name:
            return JsonResponse({'error': '画像名が提供されていません'}, status=400)

        # ファイルパスの生成
        image_path = os.path.join(settings.BASE_DIR, 'static', 'images', img_name)
        print('image_path:', image_path)  # デバッグ用ログ

        try:
            # ファイルの存在確認と削除
            if os.path.exists(image_path):
                os.remove(image_path)
                print(f'{img_name} を削除しました')  # デバッグ用ログ

                return redirect('AdminApp:next_img_list') 
            else:
                return JsonResponse({'error': '指定された画像が存在しません'}, status=404)

        except Exception as e:
            print(f'エラー発生: {str(e)}')  # デバッグ用ログ
            return JsonResponse({'error': str(e)}, status=500)
    
    # POST メソッド以外の場合
    return JsonResponse({'error': '無効なリクエストです'}, status=400)
#--------------------------------画像追加・削除--------------------------------


#--------------------------------課題問題・解答追加編集----------------------------------------
#入力された課題番号に文字が含まれていないかチェック
def check_number(number):
    try:
        number = str(number).translate(str.maketrans({
            '０': '0', '１': '1', '２': '2', '３': '3', '４': '4',
            '５': '5', '６': '6', '７': '7', '８': '8', '９': '9'
        }))
        float(number)

        numbers = re.findall(r'\d+', number)
        print(numbers)

        
        return True, str(''.join(numbers))
    except ValueError:
        print("ValueError")
        return False,number
    
# def re_check_number(number):
#     try:
#         if ('b' in number) or ('a' in number) or ('t' in number):
            
#         number = str(number).translate(str.maketrans({
#             '０': '0', '１': '1', '２': '2', '３': '3', '４': '4',
#             '５': '5', '６': '6', '７': '7', '８': '8', '９': '9'
#         }))
#         float(number)

#         numbers = re.findall(r'\d+', number)
#         print(numbers)

        
#         return True, str(''.join(numbers))
#     except ValueError:
#         print("ValueError")
#         return False,number


prefix = ""
#プレフィックスの追加（チュートリアル：t、基本問題：b、応用問題：a）
def create_number(kadai):
    global prefix
    if kadai.number:  # numberが空でないとき
        if kadai.category:
            # プレフィックスが既に含まれていない場合にのみプレフィックスを追加
            if not (kadai.number.startswith('b') or kadai.number.startswith('a') or kadai.number.startswith('t')):
                # プレフィックス設定
                category_prefix = 'b' if kadai.category == '基本区分'else ('t' if kadai.category == 'チュートリアル' else 'a')
                # プレフィックスと番号を組み合わせて設定
                prefix = f"{category_prefix}{kadai.number}"
                kadai.number = f"{category_prefix}{kadai.number}"


def add_kadai_and_answer(request, kadai_id=None):
    
    if kadai_id:
        kadai = get_object_or_404(Kadai, id=kadai_id)
        answers = Answer.objects.filter(kadai=kadai)
    else:
        kadai = None
        answers = []

    # 問題フォーム
    if request.method == "POST":
        kadai_form = KadaiForm(request.POST, instance=kadai)
        answer_form = AnswerForm(request.POST)  # 解答フォーム
        
        if kadai_form.is_valid():
            kadai_instance = kadai_form.save(commit=False)  # 問題データを保存前のインスタンス取得
            result,number = check_number(kadai_instance.number)
            if result:
                print("go")
                kadai_instance.number = number
                create_number(kadai_instance)
                global prefix
                print(prefix)

                # 新規作成時、重複チェックを実施
                if not kadai and Kadai.objects.filter(number=prefix).exists():
                    kadai_form.add_error('number', 'この問題番号は既に存在します。')
                    
                    
                
                if kadai_form.is_valid():  # 再度バリデーションチェック
                    create_number(kadai_instance)  # プレフィックスを生成する関数（詳細は気にしない）
                    kadai_instance.save()  # 問題データの保存

                    # 解答フォームが有効な場合にのみ解答を保存
                    if answer_form.is_valid():
                        answer_instance = answer_form.save(commit=False)
                        answer_instance.kadai = kadai_instance  # 解答を問題に関連付け
                        answer_instance.save()

                    return redirect('AdminApp:admin_kadai_list')  # 遷移先に適宜変更
            else:
                print("out")
                kadai_form.add_error('number', '問題番号に数字以外が含まれています。')

    else:
        kadai_form = KadaiForm(instance=kadai)
        answer_form = AnswerForm()

    return render(request, 'kadai/Kadai_add.html', {
        'kadai_form': kadai_form,
        'answer_form': answer_form,
        'kadai': kadai,
        'answers': answers,
    })


def edit_kadai_and_answers(request, kadai_id):
    kadai = get_object_or_404(Kadai, number=kadai_id)
    answers = Answer.objects.filter(kadai=kadai)

    if request.method == "POST":
        kadai_form = KadaiForm(request.POST, instance=kadai)
        answer_formset = AnswerFormSet(request.POST, queryset=answers)

        if kadai_form.is_valid() and answer_formset.is_valid():
            kadai_instance = kadai_form.save(commit=False)
            result,number = check_number(kadai_instance.number)
            if result:
                kadai_instance.number = number
                create_number(kadai_instance)  # プレフィックス再設定
                kadai_instance.save()

                # 解答フォームセットの保存
                instances = answer_formset.save(commit=False)
                for instance in instances:
                    instance.kadai = kadai_instance
                    instance.save()

                # 削除された解答を削除
                for deleted_instance in answer_formset.deleted_objects:
                    deleted_instance.delete()

                return redirect('AdminApp:admin_kadai_list')
            
            else:
                kadai_form.add_error('number', '問題番号に数字以外が含まれています。')

    else:
        kadai_form = KadaiForm(instance=kadai)
        answer_formset = AnswerFormSet(queryset=answers)

    return render(request, 'kadai/Kadai_edit.html', {
        'kadai_form': kadai_form,
        'answer_formset': answer_formset,
        'kadai': kadai,
    })


#--------------------------------課題問題・解答追加編集----------------------------------------

#------------------------------------課題管理------------------------------------------

def admin_kadai_list(request):
    kadais_by_category = Kadai.objects.values('category').distinct()  # カテゴリごとにグループ化
    categories = {}
    for category in kadais_by_category:
        category_name = category['category']
        categories[category_name] = Kadai.objects.filter(category=category_name)

    return render(request, 'kadai/Kadai_admin_list.html', {'categories': categories})

def delete_kadai(request, kadai_id):
    # 複数のKadaiオブジェクトが返ってくることに対応
    kadais = Kadai.objects.filter(number=kadai_id)
    
    if kadais.exists():
        # 1つだけ削除する（最初の1件）
        kadai = kadais.first()
        kadai.delete()
        return redirect('AdminApp:admin_kadai_list')  # 遷移先に適宜変更
    else:
        raise Http404("問題が見つかりません")
    
#------------------------------------課題管理------------------------------------------
