from django.shortcuts import render, HttpResponse

# Create your views here.

def homedash_home(request):
    return render(request, "homedash/index.html")