##############################
# IF I TOUCH THIS FILE I NEED TO MAKE MIGRATIONS THEN MIGRATE
##############################
from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    classification = models.CharField(max_length=100, blank=False, default= 'Freshman') 
    current_grade = models.CharField(max_length=100, default= '80%')

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)
    time = models.CharField(max_length=100, default= '8:00am- 9:15am')
    start = models.CharField(max_length=100, blank=False, default= '08-15-2022')
    end = models.CharField(max_length=100,blank= False, default= '12-15-2022')
    students = models.ManyToManyField(Student, 
    through = 'Enrollment')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default = False)

    def __str__(self):
        return self.name

class Enrollment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    start = models.CharField(max_length=100, blank=False, default= '08-15-2022')
    end = models.CharField(max_length=100,blank= False, default= '12-15-2022')
    current_grade = models.CharField(max_length=1, blank=True, null= True)
    instructor: models.CharField(max_length=100)
    students = models.ForeignKey(Student, on_delete=models.CASCADE)
    class Meta:
        unique_together= [['students','course']]
