from rest_framework import generics
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer


class ProductList(generics.ListCreateAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        category = self.request.query_params.get('category')
        if category is not None:
            queryset = queryset.filter(productCategory=category)
        return queryset



class ProductDetail(generics.RetrieveUpdateDestroyAPIView): 
    serializer_class = ProductSerializer
    queryset = Product.objects.all()



class CategoryList(generics.ListCreateAPIView): 
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
     

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView): 
    serializer_class = CategorySerializer
    queryset = Category.objects.all()     