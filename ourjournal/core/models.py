from django.db import models


# Create your models here.
class NameModel(models.Model):

    name = models.CharField(max_length=40)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name