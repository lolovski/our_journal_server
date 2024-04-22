from django.contrib import admin
from .models import *


class HomeworkAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'lesson', 'class_user', 'week', 'author', 'weekday')
    search_fields = ('text',)
    list_filter = ('lesson', 'class_user', 'week')
    empty_value_display = '-пусто-'


admin.site.register(Homework, HomeworkAdmin)
# Register your models here.
