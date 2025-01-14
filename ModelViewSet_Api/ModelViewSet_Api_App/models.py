from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200, null=True)
    author = models.CharField(max_length=200, null=True)
    isbn = models.CharField(max_length=13, null=True, unique=True)
    price = models.DecimalField(max_length=10,decimal_places=2, null=True)
    publish_date = models.DateField(null=True)
    
    def __str__(self):
        return self.title
