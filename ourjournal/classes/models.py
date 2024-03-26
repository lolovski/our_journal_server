from django.db import models
from core.models import NameModel

# Create your models here.


class School(NameModel):
    ...


class Class(NameModel):

    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='classes', null=True, blank=True)
    count_students = models.IntegerField()

    def __str__(self):
        return f"{self.school.name} {self.name}"


class Lesson(NameModel):

    ...


class Day(NameModel):

    ...


class Shedule(models.Model):

    class_user = models.ForeignKey(Class, on_delete=models.CASCADE, verbose_name="Класс", null=True, blank=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name="Урок", default='clean', blank=True)
    day = models.ForeignKey(Day, on_delete=models.CASCADE, verbose_name='День недели', null=True, blank=True)
    number = models.IntegerField(blank=True, default=0,)

    def __str__(self):
        return f"{self.lesson} {self.day} {self.class_user}"

