from rest_framework import serializers
from myapp.models import studentModel

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = studentModel
        fields = ['id','name','email','address']
