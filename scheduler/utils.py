from datetime import datetime, timedelta

def arrange_tasks(user, date, free_time_slots, tasks):
    """
    Arrange tasks for the user on the given date within available free time slots.
    - free_time_slots: list of tuples (start_time, end_time) for free slots
    - tasks: list of task objects sorted by priority (highest first)

    The function will try to assign scheduled_start_time and scheduled_end_time for each task.
    Unscheduled tasks are marked as pending.
    """

    free_slots = free_time_slots[:]  # Copy to avoid modifying original
    for task in tasks:
        task_duration = task.expected_duration
        allocated = False

        for i, (start, end) in enumerate(free_slots):
            available_duration = datetime.combine(date, end) - datetime.combine(date, start)
            if available_duration >= task_duration:
                task.scheduled_start_time = start
                task.scheduled_end_time = (datetime.combine(date, start) + task_duration).time()
                task.pending = False
                task.save()

                # Update free slots by subtracting allocated time
                new_start = task.scheduled_end_time
                if new_start < end:
                    free_slots[i] = (new_start, end)
                else:
                    free_slots.pop(i)
                allocated = True
                break
        
        if not allocated:
            task.pending = True
            task.scheduled_start_time = None
            task.scheduled_end_time = None
            task.save()
