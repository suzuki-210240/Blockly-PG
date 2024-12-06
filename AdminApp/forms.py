from django import forms
from .models import Task
from .models import FileUpload
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User, Group

class TaskForm(forms.ModelForm):
    file_upload = forms.FileField(
        label='課題ファイル', 
        help_text='HTML または Pythonファイルをアップロードしてください'
    )

    class Meta:
        model = Task
        fields = ['title', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.RadioSelect(),
        }
    
    def clean_file_upload(self):
        file = self.cleaned_data.get('file_upload')
        if file:
            ext = file.name.split('.')[-1].lower()
            if ext not in ['html', 'py']:
                raise forms.ValidationError('HTMLまたはPythonファイルのみアップロードできます。')
        return file
    
#--------------------------教材ファイル新規追加--------------------------------
 
class AddMaterialForm(forms.Form):
    title = forms.CharField(
        label='教材タイトル',
        max_length=40,
        required=True,
        error_messages={
            'required': '教材タイトルを入力してください。',
            'max_length': '教材タイトルは40文字以内で入力してください。',
        }
    )
    html_file_name = forms.CharField(
        max_length=200,
        required=False
    )


def clean_title(self):
    title = self.cleaned_data.get('title')

def clean_file(self):
    file = self.cleaned_data.get('file')

    # ファイルが選択されているか確認
    if not file:
        raise ValidationError('ファイルを選択してください。')

    # ファイルの種類を検証 
    if not file.name.endswith('.html'):
        raise ValidationError('HTMLファイルのみアップロード可能です。')
    return file

#--------------------------教材ファイル新規追加--------------------------------


#アカウント情報管理用
class UserGroupForm(forms.Form):
    user = forms.ModelChoiceField(queryset=User.objects.all(), required=True)
    group = forms.ModelChoiceField(queryset=Group.objects.all(), required=True)