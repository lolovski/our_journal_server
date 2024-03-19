from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from users.forms import CustomUserCreationForm, CustomUserChangeForm

from users.models import User, Status


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('class_user', 'first_name', 'middle_name', 'last_name')}),
        ('Permissions', {'fields': ('status',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'Class_id', 'password1', 'password2'),
        }),
    )

    list_display = ["first_name", "middle_name", "last_name", "username", "email", "status", "class_user"]


class CustomStatusAdmin(admin.ModelAdmin):
    list_display = ["pk", "name"]
    search_fields = ["pk"]
    list_filter = ["name"]


admin.site.register(User, CustomUserAdmin)
admin.site.register(Status, CustomStatusAdmin)