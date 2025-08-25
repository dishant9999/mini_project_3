from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

# college_project/urls.py

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', include('users.urls')),
    path('timetable/', include('timetable.urls')),
    path('scheduler/', include('scheduler.urls')),    # Make sure this is present
    # add location if needed
]

