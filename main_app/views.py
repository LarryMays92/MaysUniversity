from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Course, Student
from django.contrib.auth.models import User
# Create your views here.
# this is just like our req inside of express
def index(request):
    return render(request, 'courses/index.html')

def course_index(request):
    courses = Course.objects.all()
    return render(request, 'courses/all_courses.html', { 'courses': courses })

def course_show(request, course_id):
    course = Course.objects.get(id=course_id)
    return render(request, 'courses/show.html', { 'course': course })

class CourseCreate(CreateView):
    model = Course
    fields = '__all__'
    success_url = '/courses'
    template_name = 'courses/course_form.html'

    def form_valid(self, form):
        #commit=False makes sure we don't save to the database
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect('/courses')

class CourseUpdate(UpdateView):
    model = Course
    fields = ['name', 'duration', 'time']
    template_name = 'courses/course_form.html'

    def form_valid(self, form):
        #commit=False makes sure we don't save to the database
        self.object = form.save(commit=False)
        self.object.save()
        return HttpResponseRedirect('/courses/' + str(self.object.pk))

class CourseDelete(DeleteView):
    model = Course
    success_url = '/courses'
    template_name = 'courses/course_confirm_delete.html'

def profile(request, username):
    user = User.objects.get(username=username)
    courses = Course.objects.filter(user=user)
    students =Student.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username, 'courses': courses})

# def student_index(request):
#     students = Student.objects.all()
#     return render(request, 'students/all_students.html', { 'students': students })

def student_show(request, student_id):
    student = Student.objects.get(id=student_id)
    return render(request, 'students/show.html', { 'student': student })

class StudentCreate(CreateView):
    model = Student
    fields = '__all__'
    success_url = '/students'
    template_name = 'students/student_form.html'

    def form_valid(self, form):
        #commit=False makes sure we don't save to the database
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect('/students')

class StudentUpdate(UpdateView):
    model = Student
    fields = ['name', 'age', 'classification']
    template_name = 'students/student_form.html'

    def form_valid(self, form):
        #commit=False makes sure we don't save to the database
        self.object = form.save(commit=False)
        self.object.save()
        return HttpResponseRedirect('/students/' + str(self.object.pk))

class StudentDelete(DeleteView):
    model = Student
    success_url = '/students'
    template_name = 'students/student_confirm_delete.html'

def profile(request, username):
    user = User.objects.get(username=username)
    courses = Course.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username, 'courses': courses})

# class Students:
#     def __init__(self, name, age, classification, emerg, permanent_record  ):
#         self.name = name
#         self.age = age
#         self.classification = classification
#         self.emerg = emerg 

# students = [
#     Students('N. Johnson', '22', 'Sophmore', '234-665-2233'),
#     Students('A. Davis', '21', 'Freshman', '478-593-1298'),
#     Students('S. Mars', '20', 'Junior', '678-435-9743'),
#     Students('L. Bennett', '24', 'Senior', '706-790-9919')
# } 

# class Courses:
#     def __init__(self, name, age, classification, emerg, permanent_record  ):
#         self.name = name
#         self.duration = duration
#         self.time = time

# courses = [
#     Courses('Intro To Public Speakin', '1st Semester', '9:30am - 10:45am'),
#     Courses('Intro To Biology', '1st Semester', '11:15am - 12:30pm'),
#     Courses('Health Wellness', '1st Semester', '1:15pm - 2:15pm'),
#     Courses('Intro To Problem Solving', '21st Semester', '2:30pm -4:15pm')
# } 