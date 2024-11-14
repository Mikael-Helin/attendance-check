from django.shortcuts import render, redirect
from .models import User
from .forms import UserRegistrationForm

def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserRegistrationForm()
    return render(request, 'attendance/register.html', {'form': form})

def user_list(request):
    users = User.objects.all()
    return render(request, 'attendance/user_list.html', {'users': users})
