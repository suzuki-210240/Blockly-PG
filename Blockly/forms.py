from django import forms
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm

#アカウント新規作成のためのフォームを定義するファイル
#Templateと組み合わせて新規登録ページを作る

class CustomUserCreationForm(UserCreationForm):
    group = forms.ModelChoiceField(queryset=Group.objects.all(), required=False)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'group']