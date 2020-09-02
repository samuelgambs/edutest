from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class PresenceControl(models.Model):
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    presence = models.BooleanField(default=False)
