from django.urls import path
from UserApp import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "UserApp"
urlpatterns = [
    path("", views.Home, name="index"), #メニュー画面
    path("kadai/", views.Kadai_list, name="kadailist"),#課題一覧
    path('kadai/<str:kadai_id>/', views.Kadai_open, name='kadai_open'),#課題表示
    path("free/", views.FreeMode,name="freemode"),#自由制作モード
    path('check-code/', views.check_code, name='check_code'),#正誤判定
    path('list/', views.list_files, name='list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)