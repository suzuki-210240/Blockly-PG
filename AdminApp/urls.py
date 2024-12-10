from django.urls import path
from AdminApp import views
from django.conf import settings
from django.conf.urls.static import static


app_name = "AdminApp"
urlpatterns = [
    path('', views.admin_menu, name="index"),   #メニュー画面
    path('account-management/', views.account_management, name='account_management'),   #アカウント情報管理ページ
    path('account-management/delete/<int:user_id>/', views.account_management_delete, name='account_management_delete'),  #アカウント削除用メソッド  
    path('admin_materials_list/', views.admin_materials_list, name='admin_materials_list'),  # 教材一覧ページ
    path('add_materials/', views.add_materials, name='add_materials'),  # 教材新規追加ページ
    path('edit_materials/', views.edit_materials, name='edit_materials'),  # 教材編集ページ
    #path('material_display/', views.material_display, name='material_display'),  # 教材表示ページ
    path('add_file/', views.add_file, name='add_file'), #教材追加関数呼び出し
    path('list_files/', views.list_files, name='list_files'), #教材一覧関数呼び出し
    path('send_material/', views.send_material, name='send_material') ,#教材表示関数呼び出し
    path('admin_kadai_list/',views.admin_kadai_list,name='admin_kadai_list'),#課題一覧
    path('add_kadai/',views.add_kadai_and_answer,name='add_kadai'),#課題追加関数呼び出し
    path('edit_kadai/<str:kadai_id>',views.edit_kadai_and_answer,name='edit_kadai'),#課題編集関数呼び出し
    path('delete_kadai/<str:kadai_id>',views.delete_kadai,name='delete_kadai'),#課題削除関数呼び出し

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)