from django.contrib import admin
from django.urls import path, include
from UserApp import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.urls import path, include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/',include('rest_framework.urls')),
    path('user-info/',views.user_info),
    path('user-info/<int:pk>',views.user_instance),
    path('user-create', views.userdata_create, name='user-create')
]
urlpatterns+=re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
urlpatterns+=re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
