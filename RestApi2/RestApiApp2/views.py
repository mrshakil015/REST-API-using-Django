from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from RestApiApp2.models import *
from RestApiApp2.serializers import *

# Create your views here.

@csrf_exempt
def student_list(request):
    if request.method == 'GET':
        objs = studentModel.objects.all()
        serializer = studentModelSerialize(objs, many=True)
        return JsonResponse(serializer.data, safe=False)
    
@csrf_exempt
def teacher_list(request):
    if request.method == 'GET':
        tobjs = teacherModel.objects.all()
        serializer = teacherSerialize(tobjs, many=True)
        return JsonResponse(serializer.data, safe=False)
    
@csrf_exempt
def dept_list(request):
    if request.method == 'GET':
        objs = departmentModel.objects.all()
        serializer = teacherSerialize(objs, many=True)
        return JsonResponse(serializer.data, safe=False)