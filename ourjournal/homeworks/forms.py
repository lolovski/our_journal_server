from django import forms

from homeworks.models import Homework, Comment


class HomeworkForm(forms.ModelForm):

    class Meta:
        model = Homework
        fields = ('text', 'image',)


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)
