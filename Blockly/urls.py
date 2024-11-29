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
<<<<<<< HEAD
    path("", views.index, name="index"),    #タイトル画面表示メソッドへ
    path("login/", LoginView.as_view(), name="login"),  #ログイン画面メソッドへ
    path("/sort", views.sort, name="sort"), #アプリを振り分けるメソッドへ
    path("logout/", LogoutView.as_view(), name="logout"),   #ログアウトするメソッドへ


    path("test/", include("App.urls")),
    path("master/", include("AdminApp.urls")),
    path("user/", include("UserApp.urls")),
    path('admin/', admin.site.urls),
=======
    path("test/", include("App.urls")), #検証用アプリケーション
    path("master/", include("AdminApp.urls")), #管理者ユーザー用アプリケーション
    path("", include("UserApp.urls")), #一般ユーザー用アプリケーション
    path('admin/', admin.site.urls), #プロジェクトの管理者画面
>>>>>>> 4e8e3a80cfd79aec6bf25f18ea00fc7714fba30d
]
