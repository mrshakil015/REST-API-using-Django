from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from AccessUserApiApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('viewAllData/',viewAllData,name='viewAllData'),
    path('viewSingleData/',viewSingleData,name='viewSingleData'),
    path('deleteData/',deleteData,name='deleteData'),
    path('insertData/',insertData,name='insertData'),
    
    
]
urlpatterns+=re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
urlpatterns+=re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
