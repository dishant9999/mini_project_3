# timetable/admin.py
from django.contrib import admin
from .models import Department, Stream, Professor, Subject, Timetable

admin.site.register(Department)
admin.site.register(Stream)
admin.site.register(Professor)
admin.site.register(Subject)
admin.site.register(Timetable)
