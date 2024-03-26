from django.contrib import admin
from .models import *


class LessonAdmin(admin.ModelAdmin):
    list_display = ('name', 'id',)
    search_fields = ('name',)
    list_filter = ('name',)


class DayAdmin(admin.ModelAdmin):
    list_display = ('name', 'id',)
    search_fields = ('name',)
    list_filter = ('name',)


class ClassAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'school')
    search_fields = ('name',)
    list_filter = ('school',)


class SheduleAdmin(admin.ModelAdmin):
    list_display = ('id', 'class_user', 'lesson', 'day', 'number',)
    search_fields = ('id', 'lesson',)
    list_filter = ('class_user', 'lesson', 'day', 'lesson')


class SchoolAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


admin.site.register(School, SchoolAdmin)
admin.site.register(Lesson, LessonAdmin)

admin.site.register(Day, DayAdmin)
admin.site.register(Class, ClassAdmin)
admin.site.register(Shedule, SheduleAdmin)
# Register your models here.
