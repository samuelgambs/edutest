from django.contrib import admin

# Register your models here.

from . import models
@admin.register(models.Student)
class StudenteAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('id', 'name')
    search_fields = ('id', 'name')


@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_filter = ('id', 'title')
    search_fields = ('id', 'title')


@admin.register(models.PresenceControl)
class PresenceControlAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'presence',)
    list_filter = ('student', 'course', 'presence',)
    search_fields = ('student', 'course', 'presence',)
