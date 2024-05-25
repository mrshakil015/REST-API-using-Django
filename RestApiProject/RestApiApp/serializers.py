from django.contrib.auth.models import Group, User
from rest_framework import serializers
from RestApiApp.models import *

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    department = serializers.CharField(max_length=30)
    email = serializers.EmailField(max_length=30)
    
    def create(self, validated_data):
        return StudentModel.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.department = validated_data.get('department',instance.department)
        instance.email = validated_data.get('email',instance.email)
        
        instance.save()
        return instance