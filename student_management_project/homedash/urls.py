from django.urls import path

from homedash import views

urlpatterns = [
    path("", views.homedash_home, name="homedash_home"),
    path('chart/', views.generate_chart, name='generate_chart'),
]