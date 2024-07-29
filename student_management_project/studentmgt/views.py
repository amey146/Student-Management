from django.shortcuts import redirect, render, HttpResponse

from studentmgt.models import Student

# Create your views here.
def student_home(request):
    return render(request, "studentmgt/student_home.html")

def student_add(request):
    if request.method=='POST':
        #retrive the user inputs
        st_id = request.POST.get("st_id")
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        dob = request.POST.get("dob")
        gender=request.POST.get("gender")
        st_email = request.POST.get("st_email")
        pr_email=request.POST.get("pr_email")
        phone = request.POST.get("phone")
        address = request.POST.get("address")

        #create an object for model class
        s=Student()
        s.st_id=st_id
        s.fname=fname
        s.lname=lname
        s.dob=dob
        s.gender=gender
        s.st_email=st_email
        s.pr_email=pr_email
        s.phone=phone
        s.address=address
        s.save()
        return redirect('/studentmgt/')
    return render(request,"studentmgt/student_add.html",{})

def delete_std(request,st_id):
    s=Student.objects.get(pk=st_id)
    s.delete()
    return redirect("/std/home")

def update_std(request,st_id):
    std=Student.objects.get(pk=st_id)
    return render(request,"std/update_std.html",{'std':std})

def do_update_std(request,st_id):
        st_id = request.POST.get("st_id")
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        dob = request.POST.get("dob")
        gender=request.POST.get("gender")
        st_email = request.POST.get("st_email")
        pr_email=request.POST.get("pr_email")
        phone = request.POST.get("phone")
        address = request.POST.get("address")

        std=Student.objects.get(pk=st_id)
        std.st_id=st_id
        std.fname=fname
        std.lname=lname
        std.dob=dob
        std.gender=gender
        std.st_email=st_email
        std.pr_email=pr_email
        std.phone=phone
        std.address=address
        std.save()
        return redirect("/std")