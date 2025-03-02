from rest_framework import serializers
from .models import Product, Category



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']

class ProductSerializer(serializers.ModelSerializer):

        category = CategorySerializer()
        category_id = serializers.PrimaryKeyRelatedField(
            queryset=Category.objects.all()
        )
        class Meta:
            model = Product
            fields = ['id', 'name', 'description', 'price', 'stock', 'category', 'category_id']


