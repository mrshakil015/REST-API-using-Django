from django.db import models

# Create your models here.

class StudentModel(models.Model):
    name = models.CharField(max_length=30)
    department = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    
    def __str__(self):
        return self.name
