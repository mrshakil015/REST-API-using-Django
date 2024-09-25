from django.db import models

# Create your models here.
class ApiModel(models.Model):
    teacher_name = models.CharField(max_length=30, null=True)
    course_name = models.CharField(max_length=50, null =True)
    course_duration = models.IntegerField(null=True)
    seat = models.IntegerField(null=True)
