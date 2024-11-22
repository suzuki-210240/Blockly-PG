from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Hello, Django!")


def test_html(request):
    return render(
        request, 
        'hello/template_test.html'
    )