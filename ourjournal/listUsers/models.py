from django.db import models
from classes.models import Class, School
from users.models import Status

# Create your models here.


class ValidUser(models.Model):
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    class_user = models.ForeignKey(Class, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.last_name} + {self.first_name}'