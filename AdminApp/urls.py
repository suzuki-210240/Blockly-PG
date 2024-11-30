from django.urls import path
from AdminApp import views
from django.conf import settings
from django.conf.urls.static import static


app_name = "AdminApp"
urlpatterns = [
    path('', views.admin_menu, name="index"),
    path('add_Materials/', views.add_Materials, name='addMaterials'),  # 教材新規追加ページ
    path('edit_Materials/', views.edit_materials, name='editMaterials'),  # 教材編集ページ
    path('add-material/', views.add_material, name='add_material'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)