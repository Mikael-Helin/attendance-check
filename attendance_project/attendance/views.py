from django.shortcuts import render, redirect
from .models import User, Attendance
from .forms import UserRegistrationForm, AttendanceCheckForm
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.http import HttpResponse

def index(request):
    return render(request, 'attendance/index.html')

def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserRegistrationForm()
    return render(request, 'attendance/register.html', {'form': form})

def remove_user(request):
    email = request.GET.get('email')
    if email:
        user = get_object_or_404(User, email=email)
        user.delete()
        return redirect('user_list')
    else:
        return HttpResponse("No email provided.", status=400)

def user_list(request):
    users = User.objects.all()
    return render(request, 'attendance/user_list.html', {'users': users})

def attendance_list(request):
    email = request.GET.get('email')
    user = get_object_or_404(User, email=email)
    attendances = Attendance.objects.filter(user=user)
    return render(request, 'attendance/attendance_list.html', {'user': user, 'attendances': attendances})

def check_attendance(request):
    if request.method == 'POST':
        form = AttendanceCheckForm(request.POST)
        if form.is_valid():
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            try:
                user = User.objects.get(firstname=firstname, lastname=lastname)
                Attendance.objects.create(user=user, timestamp=timezone.now())
                messages.success(request, "Attendance recorded successfully!")
            except User.DoesNotExist:
                messages.error(request, "User not found. Please register first.")
            return redirect('check_attendance')
    else:
        form = AttendanceCheckForm()
    return render(request, 'attendance/check.html', {'form': form})


