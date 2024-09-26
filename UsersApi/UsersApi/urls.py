from django.contrib import admin
from django.urls import path, include
from UserApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/',include('rest_framework.urls')),
    path('user-info/',views.user_info),
    path('user-info/<int:pk>',views.user_instance),
    path('user-create', views.userdata_create, name='user-create')
]
