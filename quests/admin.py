from django.contrib import admin

from .models import *


class CreateAdmin(admin.ModelAdmin):
    model = CreateQuestboard


class AddAdmin(admin.ModelAdmin):
    model = AddQuest


admin.site.register(CreateQuestboard, CreateAdmin)
admin.site.register(AddQuest, AddAdmin)
