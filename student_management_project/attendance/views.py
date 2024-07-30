from django.shortcuts import redirect, render, HttpResponse
from django.utils import timezone
from attendance.models import Attendance
from studentmgt.models import Student

# Create your views here.

def attendance_home(request):
    today = timezone.now().date()
    existing_attendance = Attendance.objects.filter(date=today)

    if existing_attendance.exists():
        # If today's attendance is already marked, display the list of students with their status
        attendance_list = existing_attendance.select_related('st_id').order_by('st_id')
        return render(request, 'attendance/attendance_list.html', {'attendance_list': attendance_list})
        # return HttpResponse("Marked for today")
    
    std=Student.objects.all()
    return render(request, "attendance/attendance_home.html",{'students':std})

def attendance_add(request):
    today = timezone.now().date()
    if request.method == 'POST':
        for key, value in request.POST.items():
            if key.startswith('status_'):
                student_id = key.split('_')[1]
                status = value
                student = Student.objects.get(pk=student_id)
                Attendance.objects.create(st_id=student, date=today, status=status)
        
        return redirect('/attendance/attendance_list')  # Redirect to the same page to show the updated list

    students = Student.objects.all()
    return render(request, 'attendance.html', {'students': students})

def attendance_list(request):
    attendance_list=Attendance.objects.all()
    return render(request, "attendance/attendance_list.html",{'attendance_list':attendance_list})