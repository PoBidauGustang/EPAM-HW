from django.db import models


class Homework(models.Model):
    text = models.TextField(blank=False)
    created = models.DateTimeField(blank=False)
    deadline = models.IntegerField(blank=False)
    teacher = models.ForeignKey("Teacher", on_delete=models.PROTECT, null=True)


class HomeworkResult(models.Model):
    homework = models.ForeignKey("Homework", on_delete=models.PROTECT, null=True)
    student = models.ForeignKey("Student", on_delete=models.PROTECT, null=True)
    solution = models.TextField(blank=False)
    created = models.DateTimeField(blank=False)
    accepted = models.BooleanField(blank=False)


class Student(models.Model):
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)


class Teacher(models.Model):
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
