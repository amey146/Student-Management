from django.shortcuts import render, HttpResponse

# Create your views here.

def attendance_home(request):
    return render(request, "attendance/attendance_home.html")

def attendance_add(request):
    return render(request, "attendance/attendance_add.html")