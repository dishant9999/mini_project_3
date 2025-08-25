from django.urls import path
from . import views

urlpatterns = [
    path('departments/', views.department_list, name='department_list'),
    path('departments/<int:department_id>/streams/', views.stream_list, name='stream_list'),
    path('streams/<int:stream_id>/timetable/', views.timetable_detail, name='timetable_detail'),
    path('streams/<int:stream_id>/timetable/detailed/', views.timetable_detailed_view, name='timetable_detailed'),
]
