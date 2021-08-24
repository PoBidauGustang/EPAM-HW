from django.db import models


class Homework(models.Model):
    """Create table Homework in db"""

    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    teacher = models.ForeignKey("Teacher", on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class HomeworkResult(models.Model):
    """Create table HomeworkResult in db"""

    homework = models.ForeignKey("Homework", on_delete=models.CASCADE)
    student = models.ForeignKey("Student", on_delete=models.CASCADE)
    solution = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    accepted = models.BooleanField()

    def __str__(self):
        return self.solution


class Student(models.Model):
    """Create table Student in db"""

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return self.first_name + self.last_name


class Teacher(models.Model):
    """Create table Teacher in db"""

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return self.first_name + self.last_name
