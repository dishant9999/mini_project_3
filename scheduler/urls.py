from django.urls import path
from . import views

urlpatterns = [
    path('', views.scheduler_view, name='scheduler_view'),
]
