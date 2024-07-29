from django.urls import path

from studentmgt import views

urlpatterns = [
    path("", views.student_home, name="student_home"),
    path("student_add", views.student_add, name="student_add"),
]