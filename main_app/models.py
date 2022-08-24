##############################
# IF I TOUCH THIS FILE I NEED TO MAKE MIGRATIONS THEN MIGRATE
##############################
from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    classification = models.CharField(max_length=100, blank=False) 

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)
    students =models.ManyToManyField(Student, through = 'Enrollment')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Enrollment(models.Model):
    students = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    start = models.CharField(max_length=100, blank=False, default= '08-15-2022')
    end = models.CharField(max_length=100,blank= False, default= '12-15-2022')
    final_grade = models.CharField(max_length=1, blank=True, null= True)
    instructor: models.CharField(max_length=100)
    
    class Meta:
        unique_together= [['students','course']]


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