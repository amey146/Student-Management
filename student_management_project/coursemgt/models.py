from django.db import models

# Create your models here.
class Course(models.Model):
    c_id = models.TextField(primary_key=True)
    cname = models.CharField(max_length=255)
    cduration = models.IntegerField()

    def __str__(self):
        return self.cname