from django.shortcuts import render, HttpResponse
from .models import *
from .serializers import *
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
import io
from rest_framework.parsers import JSONParser

# Create your views here.
#----Qyeryset--------
def apimodel_info(request):
    #---complex data
    apidata = ApiModel.objects.all()
    #---python dict
    serializer = ApiModelSerializer(apidata, many=True)
    #---render Json
    json_data = JSONRenderer().render(serializer.data)
    #----Json sent to user
    return HttpResponse(json_data, content_type='application/json')


#------Model Instance
def apimodel_instance(request,pk):
    #---complex data
    apidata = ApiModel.objects.get(id=pk)
    #---python dict
    serializer = ApiModelSerializer(apidata)
    #---render Json
    json_data = JSONRenderer().render(serializer.data)
    #----Json sent to user
    return HttpResponse(json_data, content_type='application/json')

@csrf_exempt
def apidata_create(request):
    if request.method == 'POST':
        json_data = request.body
        #json to stream convert
        stream = io.BytesIO(json_data)
        #stream to python
        pythondata = JSONParser().parse(stream)
        #python to complex
        serializer = ApiModelSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Successfully insert data'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type ='application.json')

@csrf_exempt
def apidata_update(request):    
    if request.method == 'PUT':
        json_data = request.body
        #---json to stream
        stream = io.BytesIO(json_data)
        #stream to python
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        apidata = ApiModel.objects.get(id=id)
        serializer = ApiModelSerializer(apidata, data=pythondata, partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Successfully update data'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type ='application.json')
            
