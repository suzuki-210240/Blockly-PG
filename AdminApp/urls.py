from django.urls import path
from AdminApp import views

app_name = "AdminApp"
urlpatterns = [
    path("", views.Home, name="index"),
]
