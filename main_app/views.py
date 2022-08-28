from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Course, Student, Enrollment
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import LoginForm
# Create your views here.
# this is just like our req inside of express
@login_required
def index(request):
    return render(request, 'courses/index.html')
@login_required
def courses_index(request):
    courses = Course.objects.all()
    return render(request, 'courses/all_courses.html', { 'courses': courses })
@login_required
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
        self.object = form.save(commit=True)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect('/courses')

class CourseUpdate(UpdateView):
    model = Course
    fields = '__all__'
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
@login_required
def profile(request, username):
    user = User.objects.get(username=username)
    courses = Course.objects.filter(user=user)
    students =Student.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username, 'courses': courses})
@login_required
def students_index(request):
    students = Student.objects.all()
    return render(request, 'students/all_students.html', { 'students': students })
@login_required
def student_show(request, student_id):
    print('student_id+++++++++++++++++++++++++++++++',student_id)
    enrolled_courses = Enrollment.objects.select_related('students').filter(students=student_id)
    print(enrolled_courses)
    for enrollment in enrolled_courses:
        print(enrollment.course)
    student = Student.objects.get(id=student_id)
    return render(request, 'students/show.html', { 'student': student, 'enrolled_courses': enrolled_courses })

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
    fields = ['name', 'gpa', 'classification']
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

# login view
def login_view(request):
    # we can use the same view for multiple HTTP requests
    # this can be done with a simple if statement
    if request.method == 'POST':
        # handle post request
        # we want to authenticate the user with the username and pw
        form = LoginForm(request.POST)
        # validate the form data
        if form.is_valid():
            # get the username and pw and save them to variables
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            # here we use django's built in authenticate method
            user = authenticate(username = u, password = p)
            # if you found a user with matching credentials
            if user is not None:
                # if that user has not been disabled by admin
                if user.is_active:
                    # use django's built in login function
                    login(request, user)
                    return HttpResponseRedirect('/user/' + str(user.username))
                else:
                    print('the account has been disabled')
            else:
                print('the username or password is incorrect')
    else:
        # the request is a get, we render the login page
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

# logout view
def logout_view(request):
    # print('####### THIS IS THE REQUEST #######')
    # print(request.user)
    logout(request)
    return HttpResponseRedirect('/login/')

# signup view
def signup_view(request):
    # if the req is a post, then sign them up
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect('/user/' + str(user.username))
    # if the req is a get, then show the form
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})

@login_required
def after_login(request):
    return HttpResponseRedirect('/user/'%request.user.id)