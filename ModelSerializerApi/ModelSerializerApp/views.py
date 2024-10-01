from django.shortcuts import render
from . models import UsersModel
from rest_framework import status
from . serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'DELETE'])
def user_info(request, pk=None):
    # Check if the request method is GET
    if request.method == 'GET':
        if pk is not None:
            try:
                # Fetch the user with the provided ID
                user = UsersModel.objects.get(id=pk)
            except UsersModel.DoesNotExist:
                return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

            # Serialize the user data
            serializer = UserSerializer(user)
            return Response(serializer.data)
        else:
            # Fetch all users if no specific ID is provided
            users = UsersModel.objects.all()
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data)

    # Check if the request method is DELETE
    if request.method == 'DELETE':
        try:
            # Fetch the user with the provided ID
            user = UsersModel.objects.get(id=pk)
        except UsersModel.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        # Delete the user
        user.delete()
        return Response({'message': 'Data successfully deleted'}, status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET','POST'])
def user_create(request):
    if request.method == 'GET':
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
        user = UsersModel.objects.get(id=id)
        serializer = UserSerializer(user,data = request.data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Full data updated'}
            return Response(res)
        return Response(serializer.errors)
    
    if request.method == 'PATCH':
        id = pk
        user = UsersModel.objects.get(id=id)
        serializer = UserSerializer(user,data = request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Partial data updated'}
            return Response(res)
        return Response(serializer.errors)