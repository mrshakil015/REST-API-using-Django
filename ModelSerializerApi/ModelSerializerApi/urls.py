from django.contrib import admin
from django.urls import path,include
from ModelSerializerApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/',include('rest_framework.urls')),
    path('user-info/',views.user_info, name='user-info'),
    path('user-info/<int:pk>',views.user_info, name='user-info'),
    path('user-update/<int:pk>',views.user_update, name='user-update'),
    
    # path('usercreate/',views.userdata_create, name='usercreate'),
]
