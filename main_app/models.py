##############################
# IF I TOUCH THIS FILE I NEED TO MAKE MIGRATIONS THEN MIGRATE
##############################
from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    time = models.CharField(max_length=50)
    # students = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=100)

    def __str__(self):
        return self.name