import re
import os,requests,urllib.parse
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.admin.views.decorators import staff_member_required
from .models import Task,Material
from .forms import TaskForm, AddMaterialForm
from django.core.files.storage import default_storage
from django.contrib.auth.models import User, Group
from .forms import UserGroupForm
from django.http import HttpResponse
from django.db import transaction, IntegrityError


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
    return render(request, 'home/admin_menu.html')

@staff_member_required
def task_list(request):
    tasks = Task.objects.filter(created_by=request.user)
    return render(request, 'adminapp/task_list.html', {'tasks': tasks})

@staff_member_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            task = form.save(commit=False)
            task.created_by = request.user
            task.file_content = request.FILES['file_upload'].read().decode('utf-8')
            task.file_type = request.FILES['file_upload'].name.split('.')[-1].lower()
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'adminapp/task_create.html', {'form': form})

@staff_member_required
def task_edit(request, task_id):
    task = get_object_or_404(Task, id=task_id, created_by=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            if 'file_upload' in request.FILES:
                task.file_content = request.FILES['file_upload'].read().decode('utf-8')
                task.file_type = request.FILES['file_upload'].name.split('.')[-1].lower()
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'adminapp/edit.html', {'form': form})


def admin_materials_list(request):
    return render(request, 'Materials/admin_materials_list.html')

def add_materials(request):
    return render(request, 'Materials/add_materials.html')

def index(request):
    return render(request, 'Materials/index.html')

def edit_materials(request):
    return render(request, 'Materials/edit_materials.html')

#def material_display(request):
    #return render(request, 'material_display.html')

def send_material(request):
    return render(request, 'Materials/material_display.html')


#----------------------------教材一覧リスト------------------------------------

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
        return render(request, 'Materials/admin_materials_list.html', {'error_message': error_message})
    except Exception as e:
        # その他の例外が発生した場合のエラーハンドリング
        files_and_dirs = []
        error_message = "エラーが発生しました。"
        return render(request, 'Materials/admin_materials_list.html', {'error_message': error_message})

    print('ファイルのurl作成')
    # ファイルのURLを作成 (エンコード処理を追加)
    file_urls = [
        os.path.join(settings.MEDIA_URL, 'uploads', urllib.parse.quote(file)) 
        for file in files_and_dirs
    ]
    # ファイル名とURLを組み合わせたタプルのリストを作成
    files_with_urls = zip(db_material_names, file_urls)
    # フォルダ内のファイルがある場合に表示
    return render(request, 'Materials/admin_materials_list.html', {'files_with_urls': files_with_urls})
#----------------------------教材一覧リスト-----------------------------------

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


#--------------------------教材ファイル新規追加--------------------------------

def add_file(request):
    
    if request.method == 'POST' and request.FILES:
        # フォームインスタンスを1回だけ作成
        form = AddMaterialForm(request.POST, request.FILES)
        
        if form.is_valid():
            # 教材タイトルの取得 
            title = form.cleaned_data['title']
            # アップロードされたファイルの取得
            uploaded_file = request.FILES['file']
            # アップロードされたファイル名の取得
            file_name = uploaded_file.name

            # トランザクションを開始
            try:
                with transaction.atomic():
                    # データベースに保存
                    Material.objects.create(
                        material_name=title,
                        html_file_name=file_name
                    )

                    # 保存先のパスを作成
                    file_path = os.path.join(settings.MEDIA_ROOT, 'uploads', uploaded_file.name)
                    # ディレクトリが存在しない場合、作成
                    os.makedirs(os.path.dirname(file_path), exist_ok=True)

                    # ファイルを保存
                    with default_storage.open(file_path, 'wb+') as destination:
                        for chunk in uploaded_file.chunks():
                            destination.write(chunk)
                
                # 正常終了時
                return render(request, 'Materials/index.html')

            except IntegrityError:
                # 一意制約違反などのデータベースエラー処理
                error_message = 'このタイトルは既に使用されています。'
                return render(request, 'Materials/add_materials.html', {'form': form, 'error_message': error_message})

            except Exception as e:
                # 他のエラー処理
                return render(request, 'Materials/add_materials.html', {'form': form, 'error_message': str(e)})

        else:
            # フォームが無効な場合、エラーメッセージとともに再レンダリング
            return render(request, 'Materials/add_materials.html', {'form': form, 'error_message': 'フォームにエラーがあります。'})
    else:
        # 初回表示時
        form = AddMaterialForm()
    return render(request, 'Materials/add_materials.html', {'form': form})
#--------------------------教材ファイル新規追加--------------------------------
 


#*********要注意**********
#-----------------------------------------------------課題編集（views.pyの編集）-----------------------------------------------------
def edit_views(request):
    views_file_path = os.path.join(settings.BASE_DIR, 'UserApp', 'views.py')  # views.pyのパス

    # 初期状態でファイルの内容を取得
    if request.method == 'GET':
        try:
            with open(views_file_path, 'r', encoding='utf-8') as file:
                view_code = file.read()
        except FileNotFoundError:
            view_code = "views.py が見つかりませんでした。"
    elif request.method == 'POST':
        # 編集した内容をPOSTで受け取り、ファイルに書き込む
        view_code = request.POST.get('view_code', '')
        try:
            with open(views_file_path, 'w', encoding='utf-8') as file:
                file.write(view_code)
        except Exception as e:
            view_code = f"エラーが発生しました: {str(e)}"

    return render(request, 'edit_view/edit.html', {'view_code': view_code})

#------------------------------------------------------------------------------------------------------------------------------------
