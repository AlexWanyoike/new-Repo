from django.db import models
import datetime as dt
# Create your models here.


class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name  = models.CharField(max_length=30)

    def __str__(self):
        return self.name
