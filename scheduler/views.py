from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm
from datetime import date as date_class

from .utils import arrange_tasks
from .models import FreeTimeSlot, Task
from datetime import date as date_class

@login_required
def scheduler_view(request):
    user = request.user
    today = date_class.today()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = user
            task.date = today
            task.save()
            # Fetch free time slots for today
            free_slots_qs = FreeTimeSlot.objects.filter(user=user, date=today).order_by('start_time')
            free_slots = [(slot.start_time, slot.end_time) for slot in free_slots_qs]
            # Fetch unscheduled tasks sorted by priority desc
            tasks = Task.objects.filter(user=user, date=today, completed=False).order_by('-priority')
            arrange_tasks(user, today, free_slots, list(tasks))
            return redirect('scheduler_view')
    else:
        form = TaskForm()

    pending_tasks = Task.objects.filter(user=user, pending=True, completed=False, date=today).order_by('-priority')
    scheduled_tasks = Task.objects.filter(user=user, pending=False, completed=False, date=today).order_by('scheduled_start_time')

    return render(request, 'scheduler/scheduler.html', {
        'pending_tasks': pending_tasks,
        'scheduled_tasks': scheduled_tasks,
        'form': form,
    })
