from django.urls import path
from AdminApp import views
from django.conf import settings
from django.conf.urls.static import static


app_name = "AdminApp"
urlpatterns = [
    path('', views.admin_menu, name="index"),   #メニュー画面
    path('account-management/', views.account_management, name='account_management'),   #アカウント情報管理ページ
    path('account-management/delete/<int:user_id>/', views.account_management_delete, name='account_management_delete'),  #アカウント削除用メソッド  
    path('admin_materials_list/', views.admin_materials_list, name='admin_materials_list'), # 教材一覧ページ 
    path('add_materials/', views.add_materials, name='add_materials'),  # 教材新規追加ページ
    path('edit_materials/', views.edit_materials, name='edit_materials'),  # 教材編集ページ
    path('delete_materials/', views.delete_materials, name='delete_materials'), # 教材削除ページ
    path('admin_list_files/', views.admin_list_files, name='admin_list_files'), # 管理者用教材一覧関数呼び出し
    path('wait/', views.wait_page, name='wait_page'), # リダイレクトページ呼び出し
    path('master/delete_img/<path:img_id>/', views.delete_img, name='delete_img'),
    path('add_img/', views.add_img, name='add_img'),   
    path('next_img_list/', views.next_img_list, name='next_img_list'), # 画像一覧関数呼び出し
    path('edit_item/', views.edit_item, name='edit_item'), # 教材編集関数呼び出し
    path('delete_item/', views.delete_item, name='delete_item'), # 教材削除関数呼び出し
    path('load/<str:file_name>/', views.load_file, name='load_file'),#埋込むの教材読み込み
    path('add_file', views.add_file, name='add_file'), # 教材追加関数呼び出し
    path('admin_kadai_list/',views.admin_kadai_list,name='admin_kadai_list'),#課題一覧
    path('add_kadai/',views.add_kadai_and_answer,name='add_kadai'),#課題追加関数呼び出し
    path('edit_kadai/<str:kadai_id>',views.edit_kadai_and_answers,name='edit_kadai'),#課題編集関数呼び出し
    path('delete_kadai/<str:kadai_id>',views.delete_kadai,name='delete_kadai'),#課題削除関数呼び出し
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)