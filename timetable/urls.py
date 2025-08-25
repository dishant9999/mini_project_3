from django.urls import path
from . import views

urlpatterns = [
    path('departments/', views.department_list, name='department_list'),
    path('departments/<int:department_id>/streams/', views.stream_list, name='stream_list'),
    path('streams/<int:stream_id>/timetable/', views.timetable_detail, name='timetable_detail'),
    path('streams/<int:stream_id>/timetable/detailed/', views.timetable_detailed_view, name='timetable_detailed'),

    # Department URLs
    path('admin/departments/', views.department_list, name='department_list'),
    path('admin/departments/add/', views.department_add, name='department_add'),
    path('admin/departments/<int:pk>/edit/', views.department_edit, name='department_edit'),
    path('admin/departments/<int:pk>/delete/', views.department_delete, name='department_delete'),

    # Stream URLs
    path('admin/streams/', views.stream_list, name='stream_list'),
    path('admin/streams/add/', views.stream_add, name='stream_add'),
    path('admin/streams/<int:pk>/edit/', views.stream_edit, name='stream_edit'),
    path('admin/streams/<int:pk>/delete/', views.stream_delete, name='stream_delete'),

    # Professor URLs
    path('admin/professors/', views.professor_list, name='professor_list'),
    path('admin/professors/add/', views.professor_add, name='professor_add'),
    path('admin/professors/<int:pk>/edit/', views.professor_edit, name='professor_edit'),
    path('admin/professors/<int:pk>/delete/', views.professor_delete, name='professor_delete'),

    # Subject URLs
    path('admin/subjects/', views.subject_list, name='subject_list'),
    path('admin/subjects/add/', views.subject_add, name='subject_add'),
    path('admin/subjects/<int:pk>/edit/', views.subject_edit, name='subject_edit'),
    path('admin/subjects/<int:pk>/delete/', views.subject_delete, name='subject_delete'),

    # Location URLs
    path('admin/locations/', views.location_list, name='location_list'),
    path('admin/locations/add/', views.location_add, name='location_add'),
    path('admin/locations/<int:pk>/edit/', views.location_edit, name='location_edit'),
    path('admin/locations/<int:pk>/delete/', views.location_delete, name='location_delete'),

    # Task URLs
    path('admin/tasks/', views.task_list, name='task_list'),
    path('admin/tasks/add/', views.task_add, name='task_add'),
    path('admin/tasks/<int:pk>/edit/', views.task_edit, name='task_edit'),
    path('admin/tasks/<int:pk>/delete/', views.task_delete, name='task_delete'),
]
