# Django REST-API

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


