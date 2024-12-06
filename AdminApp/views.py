import re
import os
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.admin.views.decorators import staff_member_required
from .models import Task
from .forms import TaskForm, AddMaterialForm, FileUploadForm
from django.core.files.storage import default_storage
from django.contrib.auth.models import User, Group
from .forms import UserGroupForm


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


def add_Materials(request):
    return render(request, 'Materials/add_Materials.html')

def index(request):
    return render(request, 'Materials/AdminApp:index.html')

def edit_materials(request):
    return render(request, 'Materials/edit_Materials.html')

#------------------------------------------教材新規追加----------------------------------------
def add_material(request):
    print('maru ')
    if request.method == 'POST' and request.FILES:
        validated = AddMaterialForm(request.POST)
        form = FileUploadForm(request.POST, request.FILES)
        print('after')
        if form.is_valid():
            # 教材タイトルの取得 sqlへ
            #title = form.cleaned_data['title']
            print('before')

            # アップロードされたファイルの取得
            uploaded_file = request.FILES['file']

            print('uploaded_file', uploaded_file)

            # 保存先のパスを作成
            file_path = os.path.join(settings.MEDIA_ROOT, 'uploads', uploaded_file.name)

            
            # ディレクトリが存在しない場合、作成
            os.makedirs(os.path.dirname(file_path), exist_ok=True)

            # ファイルを保存
            with default_storage.open(file_path, 'wb+') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)

            return render(request, 'Materials/index.html')    
        else:
            # フォームが無効な場合の処理
            return render(request, 'Materials/add_Materials.html', {'form': form})
    else:
        # 初回表示時
        form = AddMaterialForm()
    return render(request, 'Materials/add_Materials.html', {'form': form})

#-------------------------------------------------------------------------------------------------------



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
