from django import forms
from .models import *

class CreateQuesboardForm(forms.ModelForm):
    class Meta:
        model = CreateQuestboard
        fields = ['name', 'description', 'stars']
