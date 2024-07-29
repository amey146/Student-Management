from django.urls import path

from quizmgt import views

urlpatterns = [
    path("", views.quiz_home, name="quiz_home"),
    path("quiz_add", views.quiz_add, name="quiz_add"),
]