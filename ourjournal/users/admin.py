from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from users.forms import CustomUserCreationForm, CustomUserChangeForm

from users.models import User, Status, Achievement, AchievementUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('class_user', 'first_name', 'middle_name', 'last_name')}),
        ('Permissions', {'fields': ('status',)}),
        ('TG data', {'fields': ('api_token', 'tg_id')})
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'Class_id', 'password1', 'password2'),
        }),
    )

    list_display = ["pk", "first_name", "middle_name", "last_name", "username", "email", "status", "class_user", 'api_token', 'tg_id',]


class CustomStatusAdmin(admin.ModelAdmin):
    list_display = ["pk", "name"]
    search_fields = ["pk"]
    list_filter = ["name"]


class AchievementAdmin(admin.ModelAdmin):
    list_display = ['pk', "name", 'image']
    search_fields = ["name"]


class AchievementUserAdmin(admin.ModelAdmin):
    list_display = ['pk', 'achievement', 'user']


admin.site.register(User, CustomUserAdmin)
admin.site.register(Status, CustomStatusAdmin)
admin.site.register(Achievement, AchievementAdmin)
admin.site.register(AchievementUser, AchievementUserAdmin)
