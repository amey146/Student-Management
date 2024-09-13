from django.urls import path

from quizmgt import views

urlpatterns = [
    path("", views.quiz_home, name="quiz_home"),
    path("quiz_add", views.quiz_add, name="quiz_add"),
    path("subject_select/<str:c_id>", views.subject_select),
    path("student_list/<str:c_id>/<str:sbname>/", views.student_list),
    path("quiz_submit/<str:sbname>", views.quiz_submit, name="quiz_submit"),
]
