
import re
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
import json,os,urllib.parse

def Home (request):

    context = {}    #ユーザー名と権限名の入れ物
    #↓ログインされていればユーザー名と権限名取得
    if request.user.is_authenticated:
        user = request.user
        group_names = [group.name for group in user.groups.all()]

        if 'admin' in group_names:
            group_display = "管理者"
        elif 'user' in group_names:
            group_display = "一般ユーザー"
        else:
            group_display = "未分類"
        
        context['user_info'] = {
            'username' : user.username,
            'group' : group_display
        }

    #↓contextと一緒にページをレンダリング
    return render(
        request,
        'home/main.html',
        context
    )

#課題一覧
def Kadai_list (request):
    return render(
        request,
        "Kadai/list.html",
    )


#------------------------------課題表示---------------------------------------------

def Kadai_open(request, kadai_id):
    message = "次の規則に沿って\n"
    if kadai_id == 1:
        message = "kadai1"
    elif kadai_id == 2:
        message = "kadai2"
    elif kadai_id == 3:
        message = message + "「こんにちは」と三回出力するループ"
    elif kadai_id == 4:
        message = "kadai4"
    elif kadai_id == 5:
        message = "kadai5"
    elif kadai_id == 6:
        message = "kadai6"
    else:
        message = "エラー"

    message = message + "\nを実装してください"
    return render(
        request,
        'Kadai/kadai.html',
        {
            'number': kadai_id,
            'message': message,
        }
    )

#------------------------------------------------------------------------------------


#-------------------------------正誤判定----------------------------------------------

#あらかじめ用意する解答/--複数行の文字列リテラル--/
CORRECT_CODE = '''
i = None


for i in range(4):
  print('こんにちは')

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

#-------------------------------------------------------------------------------------

#フリーモード
def FreeMode (request):
    return render(
        request,
        'free/Free.html',
    )


#--------------------------教材一覧リスト--------------------------------

def list_files(request):
    # uploadsディレクトリのパス
    folder_path = os.path.join(settings.MEDIA_ROOT, 'uploads')

    # フォルダ内のファイルとディレクトリを取得
    try:
        files_and_dirs = os.listdir(folder_path)
    except FileNotFoundError:
        # フォルダが存在しない場合のエラーハンドリング
        files_and_dirs = []
        error_message = "指定されたフォルダが見つかりませんでした。"
        return render(request, '.html', {'error_message': error_message})

    # ファイルのURLを作成 (エンコード処理を追加)
    file_urls = [
        os.path.join(settings.MEDIA_URL, 'uploads', urllib.parse.quote(file)) 
        for file in files_and_dirs
    ]
    # ファイル名とURLを組み合わせたタプルのリストを作成
    files_with_urls = zip(files_and_dirs, file_urls)

    # フォルダ内のファイルがある場合に表示
    return render(request, 'list_files.html', {'files_with_urls': files_with_urls})


#-----------------------------------------------------------------------
