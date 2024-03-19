from datetime import datetime, date

from django.db import models

from classes.models import Class, Shedule

from users.models import User

now = datetime.now()

# Create your models here.


class Homework(models.Model):

    class_user = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='homeworks', verbose_name="Класс")
    text = models.TextField()
    lesson = models.ForeignKey(Shedule, on_delete=models.CASCADE, related_name='homeworks', verbose_name="Урок")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='homeworks')
    week = models.DateField(default=date(now.year, now.month, now.day - now.weekday()), db_index=True)
    image = models.ImageField(upload_to='homeworks/', null=True, blank=True)

    def __str__(self):
        return f"{self.lesson} + {self.pk} + {self.week.month} + {self.week.day}"


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