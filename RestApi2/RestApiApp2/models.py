from django.db import models

# Create your models here.

class studentModel(models.Model):
    name = models.CharField(max_length=100,null=True)
    email = models.EmailField(max_length=100,null=True)
    department = models.CharField(max_length=100,null=True)
    
    def __str__(self):
        return self.name
    
class teacherModel(models.Model):
    tname = models.CharField(max_length=100,null=True)
    city =  models.CharField(max_length=100,null=True)
    age = models.CharField(max_length=100,null=True)
    
    def __str__(self):
        return self.tname
    
class departmentModel(models.Model):
    deptName = models.CharField(max_length=100,null=True)
    head =  models.CharField(max_length=100,null=True)
    
    def __str__(self):
        return self.deptName