from django.shortcuts import render, get_object_or_404, redirect
from django.forms import ModelForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.

def index(request):
    #Blocklyアプリのタイトル画面を表示
    return HttpResponse("<h1>タイトル画面</h1>")

@login_required
def sort(request):
    #ログインしたユーザーの所属グループによってアプリを振り分ける
    #userグループに所属しているならユーザーの、adminグループに所属しているなら管理者のメニュー画面へリダイレクト
    if request.user.groups.filter(name="user").exists():
        return redirect(UserApp:menyu)
    else:
        return redirect(AdminApp:menyu)



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