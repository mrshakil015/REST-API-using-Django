from django.contrib import admin
from django.urls import path
from AccessUserApiApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('viewAllData/',viewAllData,name='viewAllData'),
    path('viewSingleData/',viewSingleData,name='viewSingleData'),
    path('deleteData/',deleteData,name='deleteData'),
    path('insertData/',insertData,name='insertData'),
    
    
]
