from django.contrib.auth.models import AbstractUser
from django.db import models
from classes.models import Class
from core.models import NameModel

# Create your models here.


class Status(NameModel):
    ...


class User(AbstractUser):
    class_user = models.ForeignKey(Class, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Класс")
    first_name = models.CharField('Имя', max_length=30)
    last_name = models.CharField('Фамилия', max_length=30, )
    middle_name = models.CharField('Отчество', max_length=30, )
    status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True, blank=True)
    REQUIRED_FIELDS = ['last_name', 'first_name', 'middle_name', 'class_user']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def is_school_admin(self):
        if self.status_id == 2:
            return True
        else:
            return False



