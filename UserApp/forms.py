from django import forms
from django.contrib.auth.models import User
from .models import Kadai,Answer
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm

class KadaiForm(forms.ModelForm):
    class Meta:
        model = Kadai
        fields = ['number', 'category', 'name' ,'q_text']
    
    def sva(self,commit=True,number=None):
        isinstance = super().save(commit=False)

        if number:
            isinstance.number = number

        if commit:
            isinstance.save()
        return isinstance


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['a_text']

#ユーザー情報変更フォーム（パスワードフィールドを非表示）
class UserUpdateForm(UserChangeForm):
    #ユーザー名を変更可能にする
    class Meta:
        model = User
        fields = ('username', ) #変更したい項目をここに追加
        exclude = ('password', )    #パスワードフィールドを非表示
    
    #パスワードフィールドをフォームから完全に除外
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        del self.fields['password']

#パスワード変更フォーム
class PasswordChangeFormCustom(PasswordChangeForm):
    pass