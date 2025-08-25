from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Department, Stream, Professor, Subject, Location, Timetable, Lesson, LectureSlot
from .forms import DepartmentForm, StreamForm, ProfessorForm, SubjectForm, LocationForm
from django.contrib import messages
from .utils import generate_timetable
from .models import Timetable, Stream, Subject, Professor, Location


def admin_required(view_func):
    return login_required(user_passes_test(lambda u: u.is_admin)(view_func))

def list_view(request, model, template, context_name):
    objects = model.objects.all()
    return render(request, template, {context_name: objects})

def add_edit_view(request, model, form_class, pk=None, template=None, context_name='form', redirect_name=None):
    instance = get_object_or_404(model, pk=pk) if pk else None
    if request.method == 'POST':
        form = form_class(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(redirect_name)
    else:
        form = form_class(instance=instance)
    return render(request, template, {context_name: form})

def delete_view(request, model, pk, template, redirect_name):
    instance = get_object_or_404(model, pk=pk)
    if request.method == 'POST':
        instance.delete()
        return redirect(redirect_name)
    return render(request, template, {model.__name__.lower(): instance})

# Department CRUD
@admin_required
def department_list(request):
    return list_view(request, Department, 'admin_dashboard/department_list.html', 'departments')

@admin_required
def department_add(request):
    return add_edit_view(request, Department, DepartmentForm, template='admin_dashboard/department_form.html', redirect_name='department_list')

@admin_required
def department_edit(request, pk):
    return add_edit_view(request, Department, DepartmentForm, pk=pk, template='admin_dashboard/department_form.html', redirect_name='department_list')

@admin_required
def department_delete(request, pk):
    return delete_view(request, Department, pk, 'admin_dashboard/department_confirm_delete.html', 'department_list')

# Stream CRUD
@admin_required
def stream_list(request):
    return list_view(request, Stream, 'admin_dashboard/stream_list.html', 'streams')

@admin_required
def stream_add(request):
    return add_edit_view(request, Stream, StreamForm, template='admin_dashboard/stream_form.html', redirect_name='stream_list')

@admin_required
def stream_edit(request, pk):
    return add_edit_view(request, Stream, StreamForm, pk=pk, template='admin_dashboard/stream_form.html', redirect_name='stream_list')

@admin_required
def stream_delete(request, pk):
    return delete_view(request, Stream, pk, 'admin_dashboard/stream_confirm_delete.html', 'stream_list')

# Professor CRUD
@admin_required
def professor_list(request):
    return list_view(request, Professor, 'admin_dashboard/professor_list.html', 'professors')

@admin_required
def professor_add(request):
    return add_edit_view(request, Professor, ProfessorForm, template='admin_dashboard/professor_form.html', redirect_name='professor_list')

@admin_required
def professor_edit(request, pk):
    return add_edit_view(request, Professor, ProfessorForm, pk=pk, template='admin_dashboard/professor_form.html', redirect_name='professor_list')

@admin_required
def professor_delete(request, pk):
    return delete_view(request, Professor, pk, 'admin_dashboard/professor_confirm_delete.html', 'professor_list')

# Subject CRUD
@admin_required
def subject_list(request):
    return list_view(request, Subject, 'admin_dashboard/subject_list.html', 'subjects')

@admin_required
def subject_add(request):
    return add_edit_view(request, Subject, SubjectForm, template='admin_dashboard/subject_form.html', redirect_name='subject_list')

@admin_required
def subject_edit(request, pk):
    return add_edit_view(request, Subject, SubjectForm, pk=pk, template='admin_dashboard/subject_form.html', redirect_name='subject_list')

@admin_required
def subject_delete(request, pk):
    return delete_view(request, Subject, pk, 'admin_dashboard/subject_confirm_delete.html', 'subject_list')

# Location CRUD
@admin_required
def location_list(request):
    return list_view(request, Location, 'admin_dashboard/location_list.html', 'locations')

@admin_required
def location_add(request):
    return add_edit_view(request, Location, LocationForm, template='admin_dashboard/location_form.html', redirect_name='location_list')

@admin_required
def location_edit(request, pk):
    return add_edit_view(request, Location, LocationForm, pk=pk, template='admin_dashboard/location_form.html', redirect_name='location_list')

@admin_required
def location_delete(request, pk):
    return delete_view(request, Location, pk, 'admin_dashboard/location_confirm_delete.html', 'location_list')

# Timetable frontend views
def timetable_department_list(request):
    departments = Department.objects.all()
    return render(request, 'timetable/department_list.html', {'departments': departments})

def timetable_stream_list(request, department_id):
    department = get_object_or_404(Department, id=department_id)
    streams = department.stream_set.all()
    return render(request, 'timetable/stream_list.html', {'department': department, 'streams': streams})

def timetable_detail(request, stream_id):
    stream = get_object_or_404(Stream, id=stream_id)
    timetable = Timetable.objects.first()  # Simplified
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

@admin_required
def generate_timetable_view(request):
    timetable = Timetable.objects.first()
    if not timetable:
        messages.error(request, "No timetable defined!")
        return redirect('department_list')

    streams = Stream.objects.all()
    subjects = Subject.objects.all()
    professors = Professor.objects.all()
    locations = Location.objects.all()

    success = generate_timetable(timetable, streams, subjects, professors, locations)

    if success:
        messages.success(request, "Timetable generated successfully.")
    else:
        messages.error(request, "Timetable generation failed.")

    return redirect('timetable_detailed')  # Adjust based on your URL name
