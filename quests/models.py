from django.db import models


class CreateQuestboard(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    stars = models.charField(widget=TextInput(attrs={'type':'number'}))
