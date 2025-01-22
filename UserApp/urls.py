from django.urls import path
from UserApp import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "UserApp"
urlpatterns = [
    path("", views.Home, name="index"), #メニュー画面
    path("help/",views.help,name="help"),
    path("user_info/", views.user_info, name='user_info'),  #ユーザー情報管理画面
    path("kadai/", views.Kadai_list, name="kadai_list"),#課題一覧
    path('kadai/<str:kadai_id>/', views.Kadai_open, name='kadai_open'),#課題表示
    path('user_list_files/', views.user_list_files, name='user_list_files'), #一般ユーザー用教材一覧関数呼び出し
    path('send_material/', views.send_material, name='send_material') ,#教材表示関数呼び出し
    path("free/", views.FreeMode,name="freemode"),#自由制作モード
    path("public_free/", views.Public_FreeMode,name="p_freemode"),#自由制作モード
    path('check-code/', views.check_code, name='check_code'),#正誤判定
    path('progress/', views.user_progress, name='progress'), #課題進捗画面
    path('load/<str:file_name>/', views.load_file, name='load_file'),#埋込むの教材読み込み
    #path('list/', views.list_files, name='list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
