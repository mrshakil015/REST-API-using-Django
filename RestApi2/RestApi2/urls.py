from django.contrib import admin
from django.urls import path
from RestApiApp2.views import *
from RestApiApp2.apiviews import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/',student_list),
    path('student_detail/<int:pk>/',student_detail),
    
    path('teacherList/',teacher_list),
    path('deptList/',dept_list),
    
    path('snippet_list/',snippet_list),
    path('snippet_detail/<int:pk>/',snippet_detail),
]
