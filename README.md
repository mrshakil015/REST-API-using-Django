# Django REST-API

<details>
<summary>Serializer</summary>

## What is Serializer?
Serializer allow complex data such as querysets and model instances to be converted to natvie python datatypes that can then be easily rendered into JSON, XML or other content types.

</details>

## Start With API
+ Create and Activate Environment
    ```text
    python-m venv env

    .\env\Scripts\activate
    ```
+ Install requirted packages:
    ```python
    pip install django
    pip install djangorestframework
    ```
+ Set up a new Django application.
    ```python
    django-admin startproject restApiProject  
    cd restApiProject
    django-admin startapp restApiApp
    ```
+ Update `settings.py` to Add `rest_framework` and `app name` to INSTALLED_APPS:
    ```python
    INSTALLED_APPS = [
    ......
    ......
    'restApiApp',
    'rest_framework',
    ]
    ```
+ Create a model into the `models.py` files:
    ```python
    class studentModel(models.Model):
        name = models.CharField(max_length=100,null=True)
        email = models.EmailField(max_length=100,null=True)
        address = models.CharField(max_length=100,null=True)
        
        def __str__(self):
            return self.name
    ```
+ Register the model into `admin.py`:
    ```python
    from restApiApp.models import studentModel

    admin.site.register(studentModel)
    ```
+ Create a new module named `serializers.py` and create a model `serializer class` under the `restApiApp` that we'll use for our data representations.:
    ```python
    from rest_framework import serializers
    from restApiApp.models import studentModel

    class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model = studentModel
        fields = ['id','name','address','email']
    ```

## Inspact Serializer Data:
If we want we can inspect all the fields in a serializer instance.
+ Open django shell into the terminal:
    ```python
    py manage.py shell
    ```
+ Then try the following command:
    + First import `StudentSerializer` from `serializers.py`:
        ```python
        from restApiApp.serializers import StudentSerializer
        ```
    + Create a object variable:
        ```python
        serializer = StudentSerializer()
        print(repr(serializer))
        ```

## Work with Django Shell:

+ Open django shell into the terminal:
    ```python
    py manage.py shell
    ```
+ Now create object:
    + import `studentModel` from model:
        ```python
        from restApiApp.models import studentModel
        ```
    + create objects:
        ```python
        obj = studentModel()
        ```
    + assign the value into the object:
        ```python
        obj.name="Md Shakil"
        obj.address="Dhaka"
        obj.email="shakil.eub.cse@gmail.com"
        ```
    + save the object:
        ```python
        obj.save()   
        ```
    + delete object:
        ```python
        obj.delete()
        ```

## Django views using Serializer class into Web:

### View API data using `JsonResponse`:
+ Edit `views.py` and import required packages:
    ```python
    from django.shortcuts import render
    from django.http import HttpResponse, JsonResponse
    from django.views.decorators.csrf import csrf_exempt
    from rest_framework.parsers import JSONParser
    ```
+ Import `serializers` and `models` from `restApiApp`:
    ```python
    from restApiApp.serializers import StudentSerializer
    from restApiApp.models import studentModel
    ```
+ Create data view function:
    ```python
    @csrf_exempt
    def student_list(request):
        if request.method == 'GET':
            objs = studentModel.objects.all()
            serializer = studentModelSerialize(objs, many=True)
            return JsonResponse(serializer.data, safe=False)
    ```

+ Create url into the `urls.py`:

    ```python
    from django.contrib import admin
    from django.urls import path
    from RestApiApp2.views import student_list
    from RestApiApp2.apiviews import studentModel

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('list/',student_list),
    ]
    ```
        
    + Import `student_list` function from `views.py` and import `studentModel` from `models.py`.

+ Create another data view function for view the individual data using primary key:
    ```python
    @csrf_exempt
    def student_detail(request, pk):
        try:
            student = studentModel.objects.get(pk=pk)
        except studentModel.DoesNotExist:
            return HttpResponse(status=404)

        if request.method == 'GET':
            serializer = studentModelSerialize(student)
            return JsonResponse(serializer.data)
    ```
+ Create url into the `urls.py`:
    ```python
    ...............
    ...............
    from RestApiApp2.views import student_detail

    urlpatterns = [
        .............
        .............
        path('student_detail/<int:pk>/',student_detail),
    ]
    ```