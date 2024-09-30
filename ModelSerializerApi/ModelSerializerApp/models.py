from django.db import models

# Create your models here.
class UsersModel(models.Model):
    name = models.CharField(max_length=50, null=True)
    username = models.CharField(max_length=50, null=True)
    email = models.EmailField(null=True)
    address = models.CharField(max_length=100, null=True)
    website = models.CharField(max_length=50, null=True)