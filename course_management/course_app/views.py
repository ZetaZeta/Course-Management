from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.dateparse import parse_date
from course_management.course_app.models import Student, Course
from django.http import HttpResponse
from django.core import serializers

# View class to add a student
class RegisterStudent(APIView):
    def post(self, request):
        data = request.data
        new_student = Student()
        new_student.name = data['name']
        new_student.save()
        return HttpResponse(status=201)

# View class to add a class
class RegisterClass(APIView):
    def post(self, request):
        data = request.data
        new_course = Course()
        new_course.title = data['title']
        new_course.start_date = parse_date(data['start_date'])
        new_course.save()
        return HttpResponse(status=201)

# Delete the student with the given ID
class DeleteStudent(APIView):
    def post(self, request):
        Student.objects.filter(pk=data["id"]).delete()

# Delete the course with the given ID
class DeleteCourse(APIView):
    def post(self, request):
        Course.objects.filter(pk=data["id"]).delete()

# Gets the info for the course(s) of the given title
class GetCourse(APIView):
    def post(self, request):
        data = request.data
        return Response(serializers.serialize("json",Course.objects.filter(title=data["title"])))

# Gets the info for the student(s) of the given name, including all courses they are in.
class GetStudent(APIView):
    def post(self, request):
        data = request.data
        return Response(serializers.serialize("json",Student.objects.filter(name=data["name"])))

# Gets the course(s) that started at the given date
class GetCourse(APIView):
    def post(self, request):
        data = request.data
        return Response(serializers.serialize("json",Course.objects.filter(start_date=parse_date(data["start_date"]))))

# Return any students in a course of the given name.
class StudentsInCourse(APIView):
    def post(self, request):
        data = request.data
        
        return Response(serializers.serialize("json", Student.objects.filter(courses__title__contains=data["course_title"])))

# Enroll a student in a course.  Missing from the spec, but necessary to test the show-all functionality.
class EnrollStudent(APIView):
    def post(self, request):
        data = request.data
        target_student = Student.objects.filter(pk=data["target_student"])[0]
        target_course = Course.objects.filter(pk=data["target_course"])[0]
        target_student.courses.add(target_course)
        return HttpResponse(status=201)
