from django.urls import path

from . import views

urlpatterns = [
    path("", views.course_home, name="course_home"),
    path("course_add", views.course_add, name="course_add"),
    path("course_delete/<str:c_id>", views.course_delete),
    path("course_update/<str:c_id>", views.course_update),
]