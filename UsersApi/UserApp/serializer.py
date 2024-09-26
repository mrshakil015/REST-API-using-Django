from rest_framework import serializers
from . models import *

class UsersModelSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True) 
    name = serializers.CharField(max_length=50)
    username = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    address = serializers.CharField(max_length=100)
    website = serializers.CharField(max_length=50)
    
    def create(self, validated_data):
        return UsersModel.objects.create(**validated_data)