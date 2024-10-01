from django.shortcuts import render
from . models import UsersModel
from . serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
# import io

@api_view(['GET','POST'])
def user_info(request, pk=None):
    if request.method == 'GET':
        #--------Get single instance-----
        id = pk
        if id  is not None:
            #--complex data
            user = UsersModel.objects.get(id=id)
            #--python dict
            serializer = UserSerializer(user)
            return Response(serializer.data)
        
        #--------Get all data--------
        #--complex data
        user = UsersModel.objects.all()
        #--python dict
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Successfully insert data'}
            return Response(res)
        return Response(serializer.errors)

@api_view(['GET','PUT','PATCH'])
def user_update(request, pk=None):
    if request.method == 'GET':
        id = pk
        if id  is not None:
            user = UsersModel.objects.get(id=id)
            serializer = UserSerializer(user)
            return Response(serializer.data)

    if request.method == 'PUT':
        id = pk
        user = UsersModel.objects.get(pk=id)
        serializer = UserSerializer(user,data = request.data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Full data updated'}
            return Response(res)
        return Response(serializer.errors)
    
    if request.method == 'PATCH':
        id = pk
        user = UsersModel.objects.get(pk=id)
        serializer = UserSerializer(user,data = request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Partial data updated'}
            return Response(res)
        return Response(serializer.errors)