
from django.db import models

class Student(models.Model):
    st_id = models.TextField(primary_key=True)
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    dob = models.DateField()
    gender = models.CharField(max_length=1)
    st_email = models.EmailField()
    pr_email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()