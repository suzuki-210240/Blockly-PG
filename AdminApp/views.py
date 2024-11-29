import re
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.http import JsonResponse
import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import Task
from .forms import TaskForm


#def Home (request):
    #return render(
        #request,
        #'home/template.html',
    #)
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
