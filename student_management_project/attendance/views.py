from django.shortcuts import redirect, render, HttpResponse
from django.utils import timezone
from attendance.models import Attendance
from studentmgt.models import Student, Course

def attendance_home(request):
    courses = Course.objects.all()
    selected_course = request.GET.get('course')
    today = timezone.now().date()

    # Check if attendance for the selected course has already been marked today
    if selected_course:
        students = Student.objects.filter(courses__c_id=selected_course)
        already_marked = Attendance.objects.filter(date=today, st_id__in=students).exists()
    else:
        students = Student.objects.all()
        already_marked = Attendance.objects.filter(date=today).exists()

    if already_marked:
        # If attendance has been marked, show the attendance list
        attendance_list = Attendance.objects.filter(date=today)
        return render(request, "attendance/attendance_list.html", {
            'attendance_list': attendance_list,
            'selected_course': selected_course,
        })

    return render(request, "attendance/attendance_home.html", {
        'courses': courses,
        'students': students,
        'selected_course': selected_course,
    })

def attendance_add(request):
    today = timezone.now().date()

    # Check if attendance has already been marked for today
    already_marked = Attendance.objects.filter(date=today).exists()

    if already_marked:
        # Redirect or display a message indicating attendance is already marked
        return HttpResponse("Attendance for today has already been recorded.")

    if request.method == 'POST':
        for key, value in request.POST.items():
            if key.startswith('status_'):
                student_id = key.split('_')[1]
                status = value
                student = Student.objects.get(pk=student_id)
                # Save attendance for today
                Attendance.objects.create(st_id=student, date=today, status=status)
        
        return redirect('/attendance/attendance_list')

    students = Student.objects.all()
    return render(request, 'attendance.html', {'students': students})

def attendance_list(request):
    today = timezone.now().date()
    attendance_list = Attendance.objects.filter(date=today)
    total_present = attendance_list.filter(status='P').count()  # Count the number of 'P' statuses
    total_present = Attendance.objects.filter(date=today, status='P').count()
    return render(request, "attendance/attendance_list.html", {
        'attendance_list': attendance_list,
        'total_present': total_present
    })

