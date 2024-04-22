from datetime import datetime, date

from django.db import models

from classes.models import Class, Shedule, Day

from users.models import User

from django.utils import timezone

now = datetime.now().date()

# Create your models here.


class Homework(models.Model):

    class_user = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='homeworks', verbose_name="Класс", null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    lesson = models.ForeignKey(Shedule, on_delete=models.CASCADE, related_name='homeworks', verbose_name="Урок", null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='homeworks', null=True, blank=True)
    week = models.DateField(default=date(now.year, now.month, now.day - now.weekday()), db_index=True)
    image = models.ImageField(upload_to='homeworks/', null=True, blank=True)
    weekday = models.CharField(max_length=32, null=True, blank=True)

    def save(
        self, *args, **kwargs
    ):
        if self.lesson and self.lesson.day:
            self.weekday = self.lesson.day.name
            super(Homework, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.lesson} {self.week.day}.{self.week.month}"


class Comment(models.Model):

    homework = models.ForeignKey(Homework, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField('Текст комментария',
        help_text='Введите текст комментария',)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарий'

    def __str__(self):
        return self.text