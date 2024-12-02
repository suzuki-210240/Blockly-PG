from django.shortcuts import render, get_object_or_404, redirect
from django.forms import ModelForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    #Blocklyアプリのタイトル画面を表示
    return render(request, 'title.html')

@login_required
def sort(request):
    #ログインしたユーザーの所属グループによってアプリを振り分ける
    #userグループに所属しているならユーザーの、adminグループに所属しているなら管理者のメニュー画面へリダイレクト
    if request.user.groups.filter(name="user").exists():
        return redirect('UserApp:index')    #ユーザー側のメニュー画面へ
    else:
        return redirect('AdminApp:index')   #管理者側のメニュー画面へ
    #エラー修正しときました　：鈴木

    #アカウント一覧（仮）↓
    """
    ・ユーザー用アカウント
        アカウント名：YakuwaMizuki
        パスワード：mizuki0111
        所属グループ：user
    ・管理者用アカウント
        アカウント名：YakuwaYudai
        パスワード：yudai0929
        所属グループ：admin
    ・スーパーユーザー
        アカウント名：210826
        パスワード：000111
    """



#↓サンプルで作った権限によってアプリを振り分けるメソッド
"""
@login_required
def index(request):
    #ユーザーが属しているグループを取得
    if request.user.groups.filter(name='user').exists():
        return redirect('sample_app:read_post')
    else:
        return redirect('ads_sample_app:read_post')
"""