from django.contrib import admin
from .models import Task, FreeTimeSlot

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'priority', 'date', 'scheduled_start_time', 'scheduled_end_time', 'completed', 'pending')

@admin.register(FreeTimeSlot)
class FreeTimeSlotAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'start_time', 'end_time')
