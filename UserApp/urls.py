from django.urls import path
from UserApp import views

app_name = "UserApp"
urlpatterns = [
    path("", views.Home, name="index"),
    path("kadai/", views.Kadai_list, name="kadailist"),
    path('kadai/<int:kadai_id>/', views.Kadai_open, name='Kadai'),
    path("free/", views.FreeMode,name="freemode"),
    path('check-code/',views.check_code, name='check_code'),
]