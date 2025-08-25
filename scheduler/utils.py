from datetime import datetime, timedelta

def arrange_tasks(user, date, free_time_slots, tasks):
    free_slots = free_time_slots[:]  # copy to avoid mutation

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
