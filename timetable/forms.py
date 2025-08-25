from django import forms
from .models import Department, Stream, Professor, Subject, Location

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name']

class StreamForm(forms.ModelForm):
    class Meta:
        model = Stream
        fields = ['department', 'name', 'semester', 'division']

class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['department', 'name', 'short_form', 'subjects', 'streams', 'weekly_lecture_hours', 'punch_in_time', 'punch_out_time']

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name', 'code', 'department', 'stream', 'semester', 'division', 'professors', 'lecture_duration', 'lectures_per_week']

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['room_number', 'room_type']
