from django import forms
from .models import *

class QuestboardForm(forms.ModelForm):
    class Meta:
        model = Questboard
        fields = ['name', 'description', 'stars']

class QuestForm(forms.ModelForm):
    class Meta:
        model = Quest
        fields = ['name', 'description', 'stars', 'everyone']

class SignUpForm(forms.Form):
	name = forms.CharField(label='sign up', max_length=80)
		