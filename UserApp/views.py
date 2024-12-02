import re

from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render

from django.utils.timezone import datetime

from django.http import HttpResponse

from django.http import JsonResponse

import json



def Home (request):

    return render(

        request,

        'home/main.html',

    )



#課題一覧

def Kadai_list (request):

    return render(

        request,

        "Kadai/list.html",

    )



#課題表示

def Kadai_open(request, kadai_id):

    if kadai_id == 1:

        message = "課題１"

    elif kadai_id == 2:

        message = "kadai2"

    elif kadai_id == 3:

        message = "書き換えeee"

    elif kadai_id == 4:

        message = "kadai4"

    elif kadai_id == 5:

        message = "kadai5"

    elif kadai_id == 6:

        message = "kadai6"

    else:

        message = "エラー"

    return render(

        request,

        'Kadai/kadai.html',

        {

            'number': kadai_id,

            'message': message,

        }

    )



#あらかじめ用意する解答

CORRECT_CODE = '''

print(10 + 10)

print(15)

'''

#正誤判定

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



#フリーモード

def FreeMode (request):   

    

    return render(

        request,

        'free/Free.html',

    )