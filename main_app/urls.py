from django.urls import path 
from . import views 

#this will be called urlpatters 

urlpatterns = [
    #this path goes to localhost/ home path 
    path('',views.index, name = 'index'),
    path('courses/', views.courses_index, name='courses_index'),
    path('courses/<int:course_id>/', views.course_show, name='courses_show'),
    path('courses/create/', views.CourseCreate.as_view(), name='course_create'),
    path('courses/<int:pk>/update/', views.CourseUpdate.as_view(), name='course_update'),
    path('courses/<int:pk>/delete/', views.CourseDelete.as_view(), name='course_delete'),
    path('user/<username>/', views.profile, name='profile'),
]