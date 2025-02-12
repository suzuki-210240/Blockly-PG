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
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("", views.index, name="index"),    #タイトル画面表示メソッドへ
    path("login/", LoginView.as_view(), name="login"),  #ログイン画面メソッドへ
    path("sort/", views.sort, name="sort"), #アプリを振り分けるメソッドへ
    path("logout/", LogoutView.as_view(), name="logout"),   #ログアウトするメソッドへ
    path("register/", views.register, name="register"), #アカウント新規作成メソッドへ
    


    path("test/", include("App.urls")), #テスト領域のURL
    path("master/", include("AdminApp.urls")),#管理者用アプリのURL-
    path("user/", include("UserApp.urls")),#一般ユーザー用アプリのURL
    path('admin/', admin.site.urls),#プロジェクト全体の管理者URL
]
