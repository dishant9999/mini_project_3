from django.urls import path
from . import views

urlpatterns = [
    path('', views.location_list, name='location_list'),
]
