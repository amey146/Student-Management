from django.shortcuts import redirect, render, HttpResponse
from django.utils import timezone
from attendance.models import Attendance
from studentmgt.models import Student, Course
from django.core.mail import send_mail
from django.conf import settings
from datetime import date
    
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
        # Debugging purpose
        # Attendance.objects.all().delete()
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
        # return render(request, 'attendance/emailsent.html')

    if request.method == 'POST':
        for key, value in request.POST.items():
            if key.startswith('status_'):
                student_id = key.split('_')[1]
                status = value
                student = Student.objects.get(pk=student_id)
                # Save attendance for today
                Attendance.objects.create(st_id=student, date=today, status=status)
                
        # Call the function to send emails to absent students
        send_absent_email(request)

        return render(request, 'attendance/emailsent.html')

    students = Student.objects.all()
    return render(request, 'attendance.html', {'students': students})


def attendance_list(request):
    today = timezone.now().date()
    attendance_list = Attendance.objects.filter(date=today)
    total_present = attendance_list.filter(status='P').count()  # Count the number of 'P' statuses
    total_present = Attendance.objects.filter(date=today, status='A')
    print(total_present)
    return render(request, "attendance/attendance_list.html", {
        'attendance_list': attendance_list,
        'total_present': total_present
    })

from django.core.mail import send_mail
from datetime import date
from .models import Attendance, Student

def send_absent_email(request):
    if request.method == 'POST':
        today = date.today()
        formatted_date = today.strftime("%d-%m-%Y")

        # Fetch all students marked as 'Absent' today
        absent_students = Attendance.objects.filter(date=today, status='A')

        # Loop through each absent student and send an email
        for record in absent_students:
            student = record.st_id
            guardian_email = student.pr_email  # Use the `pr_email` field from the Student model
            student_name = f"{student.fname} {student.lname}"  # Combine first and last names
            
            # Format the message with the student's name
            message = f'''Dear Parent/Guardian,
This is to inform you that your ward, {student_name}, was absent from class today, {formatted_date}.
Please contact us if you have any questions.

Thank you,
Utkarsh Minds
E-mail: pranav.nerurkar@utkarshminds.com
Phone: +91 (0) 961-999-7797
Fax: +91 (0) 456 7891 
'''

            send_mail(
                subject='Attendance Report',
                message=message,
                from_email='settings.EMAIL_HOST_USER',
                recipient_list=[guardian_email],
                fail_silently=False
            )
    
    return render(request, 'attendance/emailsent.html')
