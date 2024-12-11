from django.shortcuts import render, get_object_or_404, redirect
from django.forms import ModelForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from .forms import CustomUserCreationForm
from django.contrib.auth import login


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

    #
#アカウント新規作成のためのメソッド
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='user')  #直接userグループを設定
            user.groups.add(group)  #選択したグループをユーザーに追加する
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')    #ログインも同時に行う
            return redirect('index')    #タイトル画面にリダイレクト
    else:
        #フォームを表示する際にグループの初期値を設定
        form = CustomUserCreationForm(initial={'group':Group.objects.get(name='user')})

    return render(request, 'registration/register.html', {'form':form})