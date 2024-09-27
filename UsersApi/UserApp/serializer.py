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
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', validated_data.email)
        instance.address = validated_data.get('address', validated_data.address)
        instance.website = validated_data.get('website', validated_data.website)
        
        instance.save()
        return instance
    