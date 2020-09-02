from django.shortcuts import render
from rest_framework import viewsets
from . serializers import PresenceControlSerializer, StudentSerializer, CourseSerializer
from . models import Student, Course, PresenceControl

# Create your views here.


class PrensenceControlViewSet(viewsets.ModelViewSet):

    queryset = PresenceControl.objects.all()
    serializer_class = PresenceControlSerializer


class StudentViewSet(viewsets.ModelViewSet):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class CourseViewSet(viewsets.ModelViewSet):

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
