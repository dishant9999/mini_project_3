from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    if request.user.is_admin:
        return render(request, 'users/admin_dashboard.html')
    else:
        return render(request, 'users/user_dashboard.html')
