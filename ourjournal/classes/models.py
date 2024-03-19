from django.db import models
from core.models import NameModel

# Create your models here.


class School(NameModel):
    ...


class Class(NameModel):

    school = models.ForeignKey(School, on_delete=models.CASCADE)


class Lesson(NameModel):

    ...


class Day(NameModel):

    ...


class Shedule(models.Model):

    class_user = models.ForeignKey(Class, on_delete=models.CASCADE, verbose_name="Класс")
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name="Урок")
    day = models.ForeignKey(Day, on_delete=models.CASCADE, verbose_name='День недели')

    def __str__(self):
        return f"{self.lesson} {self.day} {self.class_user}"