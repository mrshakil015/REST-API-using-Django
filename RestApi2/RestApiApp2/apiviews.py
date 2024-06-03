from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import studentModel
from .serializers import studentModelSerialize


@api_view(['GET', 'POST'])
def snippet_list(request):
    if request.method == 'GET':
        s = studentModel.objects.all()
        serializer = studentModelSerialize(s, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = studentModelSerialize(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = studentModel.objects.get(pk=pk)
    except studentModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = studentModelSerialize(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = studentModelSerialize(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)