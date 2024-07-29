from django.urls import path

from . import views

urlpatterns = [
    path("", views.attendance_home, name="attendance_home"),
    path("attendance_add", views.attendance_add, name="attendance_add"),
]