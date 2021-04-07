from django import forms
from .models import *

class CreateQuestboardForm(forms.ModelForm):
    class Meta:
        model = CreateQuestboard
        fields = ['name', 'description', 'stars']
