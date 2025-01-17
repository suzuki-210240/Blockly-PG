from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.contrib.auth.models import User, Group
from django.forms import modelformset_factory
from .models import Kadai, Answer,KadaiProgress,Material

# class TaskForm(forms.ModelForm):
#     file_upload = forms.FileField(
#         label='課題ファイル', 
#         help_text='HTML または Pythonファイルをアップロードしてください'
#     )

#     class Meta:
#         model = Task
#         fields = ['title', 'category']
#         widgets = {
#             'title': forms.TextInput(attrs={'class': 'form-control'}),
#             'category': forms.RadioSelect(),
#         }
    
#     def clean_file_upload(self):
#         file = self.cleaned_data.get('file_upload')
#         if file:
#             ext = file.name.split('.')[-1].lower()
#             if ext not in ['html', 'py']:
#                 raise forms.ValidationError('HTMLまたはPythonファイルのみアップロードできます。')
#         return file
    
#--------------------------教材ファイル新規追加--------------------------------

class ValidateMaterialForm(forms.Form):
    title = forms.CharField(
        label='教材タイトル',
        max_length=40,
        required=True,
        error_messages={
            'required': '教材タイトルを入力してください。',
            'max_length': '教材タイトルは40文字以内で入力してください。',
        },
        validators=[
            RegexValidator(
                regex=r'^[ぁ-ゔァ-ヴー々〆〤一-龥a-zA-Z0-9!#$%&\'*+/=?^_`{|}~-]+$',
                message='タイトルに使用できるのは日本語、半角英数字、一部の特殊文字のみです。'
            )
        ]
    )

    html_file = forms.FileField(
        label='教材ファイル',
        required=True,
        error_messages={
            'required': '教材ファイルを選択してください。',
        }
    )

    # タイトルのクリーンメソッド
    def clean_title(self):
        title = self.cleaned_data.get('title')
        return title

    # ファイルのクリーンメソッド
    def clean_html_file(self):
        file = self.cleaned_data.get('html_file')

        # ファイルが選択されているか確認
        if not file:
            raise ValidationError('ファイルを選択してください。')

        # ファイルの種類を検証 (HTMLファイルのみ許可)
        if not file.name.endswith('.html'):
            raise ValidationError('HTMLファイルのみアップロード可能です。')

        return file

#--------------------------教材ファイル新規追加--------------------------------

#------------------------------課題関係----------------------------------------

class KadaiForm(forms.ModelForm):
    class Meta:
        model = Kadai
        fields = ['number', 'category', 'name' ,'q_text']
    
    def save(self,commit=True,number=None):
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

AnswerFormSet = modelformset_factory(
    Answer,
    form=AnswerForm,
    fields=['a_text'],
    extra=1,  # 新規解答用の空フォームを1つ追加
    can_delete=True  # 解答の削除を可能にする
)

class KadaiProgressForm(forms.ModelForm):
    class Meta:
        model = KadaiProgress
        fields = ['user', 'kadai', 'progress']

#------------------------------課題関係----------------------------------------

#アカウント情報管理用
class UserGroupForm(forms.Form):
    #ユーザーを選択するフィールド（スーパーユーザーを除外）
    user = forms.ModelChoiceField(queryset=User.objects.exclude(is_superuser=True), label="ユーザー名")

    #グループを選択するフィールド
    group_choices = [
        ('user', '一般ユーザー'),
        ('admin', '管理者'),
    ]
    group = forms.ChoiceField(choices=group_choices, label="権限")