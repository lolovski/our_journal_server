from django.contrib import admin

from .models import ValidUser

# Register your models here.


class ValidUserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'middle_name', 'class_user', 'school')
    search_fields = ('first_name', 'last_name')
    list_filter = ('class_user', 'school')


admin.site.register(ValidUser, ValidUserAdmin)