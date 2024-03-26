from functools import wraps

from django.http import HttpResponseForbidden, HttpResponseRedirect


def school_admin_required(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        user = request.user
        if user.status.name == 'школьный админ':
            return func(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/')
    return wrapper