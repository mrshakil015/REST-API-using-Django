from django.shortcuts import render, HttpResponse
from .models import *
from .serializers import *
from rest_framework.renderers import JSONRenderer

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
