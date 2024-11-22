from django.urls import path
from App import views

urlpatterns = [
    path("",views.home, name="home"),
    path("hello/<name>",views.hello_there, name="hello_there"),
    path("test", views.test_page,name="test"),
    path('check-code/',views.check_code, name='check_code'),
]


