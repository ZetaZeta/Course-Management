"""course_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from course_management.course_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/student/', views.RegisterStudent.as_view()),
    path('register/class/', views.RegisterClass.as_view()),
    path('course/students/', views.StudentsInCourse.as_view()),
    path('course/', views.GetCourse.as_view()),
    path('student/', views.GetStudent.as_view()),
    path('delete/course/', views.DeleteCourse.as_view()),
    path('delete/student/', views.DeleteStudent.as_view()),
    path('enroll/', views.EnrollStudent.as_view()),
]
