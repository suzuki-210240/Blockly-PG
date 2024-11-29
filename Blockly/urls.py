"""
URL configuration for Blockly project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include,path
from AdminApp import views
urlpatterns = [
    path("test/", include("App.urls")), #検証用アプリケーション
    path("master/", include("AdminApp.urls")), #管理者ユーザー用アプリケーション
    path("", include("UserApp.urls")), #一般ユーザー用アプリケーション
    path('admin/', admin.site.urls), #プロジェクトの管理者画面
    #path('', include('social_django.urls', namespace='social')),
    path('admin/menu/', views.admin_menu, name='admin_menu'),
    path('admin/tasks/', views.task_list, name='task_list'),
    path('admin/tasks/create/', views.task_create, name='task_create'),
    path('admin/tasks/edit/<int:task_id>/', views.task_edit, name='task_edit'),
]
