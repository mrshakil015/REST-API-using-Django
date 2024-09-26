from rest_framework import serializers
from .models import *

class ApiModelSerializer(serializers.Serializer):
    teacher_name = serializers.CharField(max_length=30)
    course_name = serializers.CharField(max_length=50)
    course_duration = serializers.IntegerField()
    seat = serializers.IntegerField()
    
    def create(self, validated_data):
        return ApiModel.objects.create(**validated_data)