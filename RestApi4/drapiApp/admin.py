from django.contrib import admin
from  .models import *

# Register your models here.
@admin.register(ApiModel)
class ApiModelAdmin(admin.ModelAdmin):
    list_display=['id','teacher_name','course_name','course_duration','seat']
