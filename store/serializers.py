from rest_framework import serializers
from .models import Product, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']

class ProductSerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField(write_only=True)
    category = serializers.StringRelatedField(read_only=True)

    class Meta:
            model = Product
            fields = ['id', 'name', 'description', 'price', 'stock', 'category', 'category_id']

    def create(self, validated_data):
        category_id = validated_data.pop('category_id')
        category = Category.objects.get(id=category_id)
        product = Product.objects.create(category=category, **validated_data)
        return product