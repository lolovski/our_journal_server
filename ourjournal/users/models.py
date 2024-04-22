from django.contrib.auth.models import AbstractUser
from django.db import models
from classes.models import Class
from core.models import NameModel

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.


class Achievement(NameModel):

    image = models.ImageField(upload_to='Achievement/', null=True, blank=True)


class Status(NameModel):
    ...


class User(AbstractUser):
    class_user = models.ForeignKey(Class, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Класс")
    first_name = models.CharField('Имя', max_length=30)
    last_name = models.CharField('Фамилия', max_length=30, )
    middle_name = models.CharField('Отчество', max_length=30, )
    status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True, blank=True)
    achievements = models.ManyToManyField(Achievement, through='AchievementUser')
    tg_id = models.CharField('Телеграм ID', max_length=32, null=True, blank=True)
    api_token = models.CharField('API token', max_length=128, null=True, blank=True)

    REQUIRED_FIELDS = ['last_name', 'first_name', 'middle_name', 'class_user']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def is_school_admin(self):
        if self.status_id == 2:
            return True
        else:
            return False

    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def create_auth_token(sender, instance=None, created=False, **kwargs):
        if created:
            Token.objects.create(user=instance)





class AchievementUser(models.Model):

    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.achievement} {self.user}'



