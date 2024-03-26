from django import forms

from classes.models import Class, Shedule


class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ('name', 'count_students')


class SheduleSchoolForm(forms.ModelForm):

    class Meta:
        model = Shedule
        fields = ('lesson', 'number')
