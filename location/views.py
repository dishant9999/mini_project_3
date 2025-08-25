from django.shortcuts import render
from .models import Location

def location_list(request):
    locations = Location.objects.all()
    return render(request, 'location/location_list.html', {'locations': locations})
