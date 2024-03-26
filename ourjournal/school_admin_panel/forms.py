from classes.models import Class, Shedule, Day, School
from django import forms
from django.contrib.auth import get_user_model


from users.forms import CustomUserCreationForm


class ClassListForm(forms.Form):

    """def __init__(self, *args, **kwargs):
        user = kwargs.pop(
            'user')
        super(ClassListForm, self).__init__(*args, **kwargs)
        self.fields['class_user'].queryset = Class.objects.filter(school=user.class_user.school.id)
    class_user = forms.ModelChoiceField(queryset=None, widget=forms.Select, required=True)"""
    count_students = forms.IntegerField()
    class_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
