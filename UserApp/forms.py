from django import forms
from django.contrib.auth.models import User
from .models import Kadai,Answer,KadaiProgress
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
        
class KadaiProgressForm(forms.ModelForm):
    class Meta:
        model = KadaiProgress
        fields = ['user', 'kadai', 'progress']





#ユーザー情報変更フォーム（パスワードフィールドを非表示）
class UserUpdateForm(UserChangeForm):
    class Meta:
        model =User
        fields = ('username', ) #変更する要素
        exclude = ('password', )    #パスワードフィールドを非表示
    
    #パスワードフィールドをフォームから完全に削除
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        del self.fields['password']

# パスワード変更フォーム
class PasswordChangeFormCustom(PasswordChangeForm):
    # 必要であれば追加の検証やカスタマイズを加えます
    pass
