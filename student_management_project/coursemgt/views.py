from django.shortcuts import redirect, render, HttpResponse

from coursemgt.models import Course

# Create your views here.

def course_home(request):
    courses = Course.objects.all()
    return render(request, "coursemgt/course_home.html", {'courses':courses})

def course_add(request):
    if request.method == 'POST':
        cid = request.POST.get("cid")
        cname = request.POST.get("cname")
        cduration = request.POST.get("cduration")
        c = Course()
        c.c_id = cid
        c.cname = cname
        c.cduration = cduration
        c.save()
        return redirect("/coursemgt")
    return render(request, "coursemgt/course_add.html", {})


def course_update(request, c_id):
    c=Course.objects.get(pk=c_id)
    return render(request, "coursemgt/course_update.html",{'c':c})

def course_delete(request, c_id):
    c=Course.objects.get(pk=c_id)
    c.delete()
    return redirect("/coursemgt")
