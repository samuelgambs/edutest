from rest_framework import serializers
from . models import PresenceControl, Student, Course


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'name')


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'title')


class PresenceControlSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)
    student = StudentSerializer(read_only=True)

    class Meta:
        model = PresenceControl
        fields = ('id', 'course', 'student', 'presence')
