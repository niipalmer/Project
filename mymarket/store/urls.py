
from django.urls import path
from .views import ProductList, ProductDetail, CategoryList, CategoryDetail

urlpatterns = [
    path('product/', ProductList.as_view()),
    path('product/<int:pk>/', ProductDetail.as_view()),
    path('category/', CategoryList.as_view()),
    path('category/', CategoryDetail.as_view()),
    
    ]