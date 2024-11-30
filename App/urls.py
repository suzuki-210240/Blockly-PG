from django.urls import path
from App import views

app_name = "App"   
urlpatterns = [
    path("",views.home, name="home"),
    path("test/", views.test_page,name="test"),
    path('check-code/',views.check_code, name='check_code')
]