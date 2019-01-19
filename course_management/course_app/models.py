from django.conf import settings
from django.db import models
import datetime

class Course(models.Model):
    title = models.CharField(max_length=255)
    start_date = models.DateField()

class Student(models.Model):
    name = models.CharField(max_length=100)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.name
