from django.db import models
import datetime

# Create your models here.
class Workers(models.Model):
    name = models.CharField(max_length = 100)
    position = models.CharField(max_length = 50) 
    description = models.TextField(default = 'Hard working')
    registration_date = models.DateField(default = datetime.date(2017,1,1))
    graduation_date = models.DateField(default = datetime.date(2017,1,1))

class Student(models.Model):
    name = models.CharField(max_length = 100)
    course = models.CharField(max_length = 50)
    description = models.TextField(default = 'Disciplined')
    registration_date = models.DateField(default = datetime.date(2017,4,19))
