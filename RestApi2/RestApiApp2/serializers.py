from rest_framework import serializers
from RestApiApp2.models import *


class studentModelSerialize(serializers.ModelSerializer):
    class Meta:
        model = studentModel
        fields = ['id','name','department','email']
        
class teacherSerialize(serializers.ModelSerializer):
    class Meta:
        model = teacherModel
        exclude = ('id', )
        
class deptSerialize(serializers.ModelSerializer):
    class Meta:
        model = departmentModel
        fields = ['id','deptName','head']
        