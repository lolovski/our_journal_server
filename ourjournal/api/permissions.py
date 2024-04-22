from django.utils import timezone
from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
            )

    def has_object_permission(self, request, view, obj):
         return obj.author == request.user


class ReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS


class IsValidDate(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return timezone.datetime.strptime(obj.week, '%Y-%m-%d').date() >= (timezone.now().date() - timezone.timedelta(days=7))



