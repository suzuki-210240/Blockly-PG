from django.urls import path
from UserApp import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "UserApp"
urlpatterns = [
    path("", views.Home, name="index"), #メニュー画面
    path("kadai/", views.Kadai_list, name="kadai_list"),#課題一覧
    path('kadai/<str:kadai_id>/', views.Kadai_open, name='kadai_open'),#課題表示
    path('list_files/', views.list_files, name='Material_list'), #教材一覧関数呼び出し
    path('send_material/', views.send_material, name='send_material') ,#教材表示関数呼び出し
    path("free/", views.FreeMode,name="freemode"),#自由制作モード
    path('check-code/', views.check_code, name='check_code'),#正誤判定
    #path('list/', views.list_files, name='list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)