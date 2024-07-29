from django.shortcuts import render, HttpResponse

# Create your views here.
def quiz_home(request):
    return render(request, "quizmgt/quiz_home.html")

def quiz_add(request):
    return render(request, "quizmgt/quiz_add.html")