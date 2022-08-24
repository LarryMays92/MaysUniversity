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
    classification = models.CharField(max_length=100, blank=True) 


    def __str__(self):
        return self.name


# reference to linking teachers with students and courses and vice versa
#many to many relationship!!

# class Person(models.Model):
#     name = models.CharField(max_length=128)

#     def __str__(self):
#         return self.name

# class Group(models.Model):
#     name = models.CharField(max_length=128)
#     members = models.ManyToManyField(Person, through='Membership')

#     def __str__(self):
#         return self.name

# class Membership(models.Model):
#     person = models.ForeignKey(Person, on_delete=models.CASCADE)
#     group = models.ForeignKey(Group, on_delete=models.CASCADE)
#     date_joined = models.DateField()
#     invite_reason = models.CharField(max_length=64)