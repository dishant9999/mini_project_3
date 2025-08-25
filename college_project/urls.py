from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('dashboard/', include('users.urls')),  # Dashboard and related views
    path('timetable/', include('timetable.urls')),
    path('location/', include('location.urls')),
    path('scheduler/', include('scheduler.urls')),
]
