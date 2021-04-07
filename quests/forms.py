from django import forms
from .models import *

class QuestboardForm(forms.ModelForm):
    class Meta:
        model = Questboard
        fields = ['name', 'description', 'stars']

class QuestForm(forms.ModelForm):
    class Meta:
        model = Quest
        fields = ['name', 'description', 'stars']
        # add missing fields (3 sign-ups or everyone)
