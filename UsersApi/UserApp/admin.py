from django.contrib import admin
from . models import UsersModel

# Register your models here.
@admin.register(UsersModel)
class UsersModelAdmin(admin.ModelAdmin):
    list_display = ['name','username','email','address','website']
