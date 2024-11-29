from django import forms
from .models import Task

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