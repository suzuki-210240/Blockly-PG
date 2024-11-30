import re
import os
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import Task
from .forms import TaskForm, AddMaterialForm, FileUploadForm
from django.core.files.storage import default_storage


@login_required
def admin_menu(request):
    return render(request, 'home/menu.html')

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
    return render(request, 'add_Materials.html')

def index(request):
    return render(request, 'AdminApp:index.html')

def edit_materials(request):
    return render(request, 'edit_Materials.html')

# 教材新規追加
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

            return render(request, 'index.html')    
        else:
            # フォームが無効な場合の処理
            return render(request, 'add_material.html', {'form': form})
    else:
        # 初回表示時
        form = AddMaterialForm()
    return render(request, 'add_material.html', {'form': form})
