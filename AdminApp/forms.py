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
    
#バリデーション関数
class AddMaterialForm(forms.Form):
    title = forms.CharField(max_length=40, min_length=2, required=True)
    file = forms.FileField(required=True)

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 2:
            raise ValidationError('教材タイトルは2文字以上で入力してください。')
        if len(title) > 40:
            raise ValidationError('教材タイトルは40文字以内で入力してください。')
        return title

    def clean_file(self):
        file = self.cleaned_data.get('file')
        if not file:
            raise ValidationError('htmlファイルを選択してください。')
        return file


#ファイルアップロード
class FileUploadForm(forms.ModelForm):
    class Meta:
        model = FileUpload
        fields = ['file']


#アカウント情報管理用
class UserGroupForm(forms.Form):
    user = forms.ModelChoiceField(queryset=User.objects.all(), required=True)
    group = forms.ModelChoiceField(queryset=Group.objects.all(), required=True)