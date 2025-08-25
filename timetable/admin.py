from django.contrib import admin
from .models import Department, Stream, Professor, Subject, Timetable

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Stream)
class StreamAdmin(admin.ModelAdmin):
    list_display = ('name', 'semester', 'division', 'department')

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_form', 'department', 'weekly_lecture_hours')

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'department', 'stream', 'semester', 'division')

@admin.register(Timetable)
class TimetableAdmin(admin.ModelAdmin):
    list_display = ('days_per_week', 'shift_start_time', 'shift_end_time', 'number_of_lectures')
