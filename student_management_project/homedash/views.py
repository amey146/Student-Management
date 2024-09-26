from django.shortcuts import render, HttpResponse

from studentmgt.models import Student

# Create your views here.

def homedash_home(request):
    # Student.objects.all().delete()
    return render(request, "homedash/index.html")