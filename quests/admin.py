from django.contrib import admin

from .models import *


class QuestboardAdmin(admin.ModelAdmin):
    model = Questboard


class QuestAdmin(admin.ModelAdmin):
    model = Quest


admin.site.register(Questboard, QuestboardAdmin)
admin.site.register(Quest, QuestAdmin)
