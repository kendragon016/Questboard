from django.contrib import admin

from .models import *


class CreateAdmin(admin.ModelAdmin):
    model = CreateQuestboard


admin.site.register(CreateQuestboard, CreateAdmin)
