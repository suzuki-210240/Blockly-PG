from django.urls import path
from UserApp import views

app_name = "UserApp"
urlpatterns = [
    path("", views.Home, name="index"), #メニュー画面
    path("kadai/", views.Kadai_list, name="kadailist"),#課題一覧
    path('kadai/<int:kadai_id>/', views.Kadai_open, name='Kadai'),#課題表示
    path("free/", views.FreeMode,name="freemode"),#自由制作モード
    path('check-code/',views.check_code, name='check_code'),#正誤判定
]