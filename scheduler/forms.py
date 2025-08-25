from django import forms
from .models import Task, FreeTimeSlot

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'priority', 'expected_duration', 'date']

class FreeTimeSlotForm(forms.ModelForm):
    class Meta:
        model = FreeTimeSlot
        fields = ['date', 'start_time', 'end_time']
