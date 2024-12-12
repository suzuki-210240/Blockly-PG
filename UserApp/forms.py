from django import forms
from django.contrib.auth.models import User
from .models import Kadai,Answer,KadaiProgress


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