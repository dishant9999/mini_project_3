from django.shortcuts import render, get_object_or_404
from .models import Department, Stream, Timetable, Lesson, LectureSlot

def department_list(request):
    departments = Department.objects.all()
    return render(request, 'timetable/department_list.html', {'departments': departments})

def stream_list(request, department_id):
    department = get_object_or_404(Department, id=department_id)
    streams = department.stream_set.all()
    return render(request, 'timetable/stream_list.html', {'department': department, 'streams': streams})

def timetable_detail(request, stream_id):
    stream = get_object_or_404(Stream, id=stream_id)
    timetable = Timetable.objects.first()  # Simplified, update as necessary
    return render(request, 'timetable/timetable_detail.html', {'stream': stream, 'timetable': timetable})

def timetable_detailed_view(request, stream_id):
    stream = get_object_or_404(Stream, id=stream_id)
    lessons = Lesson.objects.all().order_by('number')
    lecture_slots = LectureSlot.objects.filter(stream=stream).select_related('lesson', 'subject', 'professor', 'location')
    slots_by_lesson = {lesson.id: [] for lesson in lessons}
    for slot in lecture_slots:
        slots_by_lesson[slot.lesson.id].append(slot)
    context = {
        'stream': stream,
        'lessons': lessons,
        'slots_by_lesson': slots_by_lesson,
    }
    return render(request, 'timetable/timetable_detailed.html', context)
