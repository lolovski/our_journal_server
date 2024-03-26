
from django import forms

from listUsers.models import ValidUser


class SchoolUserForm(forms.ModelForm):
    class Meta:
        model = ValidUser
        fields = ['last_name', 'first_name', 'middle_name']



