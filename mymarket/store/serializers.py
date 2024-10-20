from rest_framework import serializers
from store.models import Product, Category

class ProductSerializer(serializers.ModelSerializers):
    class Meta:
        model = Product
        fields = ('__all__')


class CategorySerializer(serializers.ModelSerializers):
    class Meta:
        model = Category
        fields = ('__all__')



