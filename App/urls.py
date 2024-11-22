from django.urls import path
from App import views

urlpatterns = [
    path("", views.home, name='home'),
    path("test", views.test_html, name='home'),
]