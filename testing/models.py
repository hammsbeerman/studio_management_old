from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=30)
    students = models.ManyToManyField(Student)

    def __str__(self):
        return self.name
