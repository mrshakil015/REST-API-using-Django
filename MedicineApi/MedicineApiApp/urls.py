from rest_framework.routers import DefaultRouter
from .views import *
from django.urls import path,include

router = DefaultRouter()
router.register(r'categories',ProductCategoryViewset,basename='category')
router.register(r'products',ProductViewSet,basename='product')

urlpatterns = [
    path('',include(router.urls)),
]