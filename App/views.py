import re
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.http import JsonResponse
import json

# Create your views here.
def home(request):
    return render(
        request,
        'main.html',
    )


def test_page(request):
    return render(
        request,
        'index.html'
    )


#あらかじめ用意する解答
CORRECT_CODE = '''
print(5 + 10)
print(15)
'''
@csrf_exempt
def check_code(request):
    global CORRECT_CODE
    if request.method == 'POST':
        # 受け取ったPythonコードを取得
        data = json.loads(request.body)
        submitted_code = data.get('code')

        # 受け取ったコードと正しい答えを比較
        if submitted_code.strip() == CORRECT_CODE.strip():
            return JsonResponse({"isCorrect": True})
        else:
            return JsonResponse({"isCorrect": False})

    return JsonResponse({"error": "POSTメソッドで送信してください"}, status=400)