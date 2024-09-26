from django.contrib import admin
from django.urls import path, include
from drapiApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('apiinfo/',views.apimodel_info),
    path('apiinfo/<int:pk>',views.apimodel_instance),
    path('apicreate/',views.apidata_create, name='apicreate'),
    path('apiupdate/',views.apidata_update, name='apiupdate'),
]
