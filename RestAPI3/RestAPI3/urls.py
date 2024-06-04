from django.contrib import admin
from django.urls import path
from myapp.views import student_list
from myapp.mixinsView import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student_list/',student_list),
    
    path('stuListMixins/',stuListMixins.as_view()),
    path('stuDetailsMixins/<int:pk>/',stuDetailsMixins.as_view()),
]
