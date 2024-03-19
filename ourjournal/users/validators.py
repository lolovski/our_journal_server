from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from listUsers.models import ValidUser


def validate_user(first_name, last_name, middle_name):
    if ValidUser.objects.filter(first_name=first_name, last_name=last_name, middle_name=middle_name):
        raise ValidationError('')

