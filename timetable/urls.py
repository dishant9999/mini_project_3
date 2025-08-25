from django.urls import path
from . import views

urlpatterns = [
    # Admin CRUD routes
    path('admin/departments/', views.department_list, name='department_list'),
    path('admin/departments/add/', views.department_add, name='department_add'),
    path('admin/departments/<int:pk>/edit/', views.department_edit, name='department_edit'),
    path('admin/departments/<int:pk>/delete/', views.department_delete, name='department_delete'),

    path('admin/streams/', views.stream_list, name='stream_list'),
    path('admin/streams/add/', views.stream_add, name='stream_add'),
    path('admin/streams/<int:pk>/edit/', views.stream_edit, name='stream_edit'),
    path('admin/streams/<int:pk>/delete/', views.stream_delete, name='stream_delete'),

    path('admin/professors/', views.professor_list, name='professor_list'),
    path('admin/professors/add/', views.professor_add, name='professor_add'),
    path('admin/professors/<int:pk>/edit/', views.professor_edit, name='professor_edit'),
    path('admin/professors/<int:pk>/delete/', views.professor_delete, name='professor_delete'),

    path('admin/subjects/', views.subject_list, name='subject_list'),
    path('admin/subjects/add/', views.subject_add, name='subject_add'),
    path('admin/subjects/<int:pk>/edit/', views.subject_edit, name='subject_edit'),
    path('admin/subjects/<int:pk>/delete/', views.subject_delete, name='subject_delete'),

    path('admin/locations/', views.location_list, name='location_list'),
    path('admin/locations/add/', views.location_add, name='location_add'),
    path('admin/locations/<int:pk>/edit/', views.location_edit, name='location_edit'),
    path('admin/locations/<int:pk>/delete/', views.location_delete, name='location_delete'),

    # Frontend timetable views
    path('departments/', views.timetable_department_list, name='timetable_department_list'),
    path('departments/<int:department_id>/streams/', views.timetable_stream_list, name='timetable_stream_list'),
    path('streams/<int:stream_id>/', views.timetable_detail, name='timetable_detail'),
    path('streams/<int:stream_id>/detailed/', views.timetable_detailed_view, name='timetable_detailed'),

    path('admin/timetable/generate/', views.generate_timetable_view, name='generate_timetable'),

]
