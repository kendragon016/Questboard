from django import forms
from .models import *

class CreateQuestboardForm(forms.ModelForm):
    class Meta:
        model = CreateQuestboard
        fields = ['name', 'description', 'stars']

class AddQuestForm(forms.ModelForm):
    class Meta:
        model = AddQuest
        fields = ['name', 'description', 'stars']
        # add missing fields (3 sign-ups or everyone)
