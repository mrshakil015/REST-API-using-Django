from django.shortcuts import render, HttpResponse
from . models import UsersModel
from . serializer import UsersModelSerializer
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
import io
from rest_framework.parsers import JSONParser

#------Reterive all data-----
def user_info(request):
    #-------complext data
    userdata = UsersModel.objects.all()
    #------python dictionary
    serializer = UsersModelSerializer(userdata, many=True)
    #-----render json
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')

#-------Reterive single instance--------
def user_instance(request, pk):
    userdata = UsersModel.objects.get(id=pk)
    serializer = UsersModelSerializer(userdata)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')

#------Create/Insert data using api into model------
@csrf_exempt
def userdata_create(request):
    if request.method == 'POST':
        json_data = request.body
        #--json to stream convert
        stream = io.BytesIO(json_data)
        #--stream to python
        pythondata = JSONParser().parse(stream)
        #--python to complex
        serializer = UsersModelSerializer(data = pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Successfully insert data'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type = 'application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type = 'application/json')