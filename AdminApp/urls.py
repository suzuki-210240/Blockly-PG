from django.urls import path
from AdminApp import views

urlpatterns = [
    path("", views.index, name="index"),
]
