from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register_user, name='register_user'),
    path('users/', views.user_list, name='user_list'),
    path('check/', views.check_attendance, name='check_attendance'),
    path('attendance/', views.attendance_list, name='attendance_list'),
    path('remove-user/', views.remove_user, name='remove_user'),
]