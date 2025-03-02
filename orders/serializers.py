from rest_framework import serializers
from .models import Order, OrderItem
from store.models import Product
from store.serializers import ProductSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    order = serializers.PrimaryKeyRelatedField(read_only=True)
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), write_only=True
    )

    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        items_data = validated_data.pop('items', [])
        order = Order.objects.create(**validated_data)

        total_price = 0
        order_items = []

        for item_data in items_data:
            product_id = item_data.get('product_id')
            quantity = item_data.get('quantity', 1)

            if not product_id:
                raise serializers.ValidationError("Mahsulot ID berilmagan!")

            try:
                product = Product.objects.get(id=product_id)
            except Product.DoesNotExist:
                raise serializers.ValidationError(f"Mahsulot ID {product_id} topilmadi!")

            price = product.price
            total_price += price * quantity


            order_items.append(
                OrderItem(order=order, product=product, price=price, quantity=quantity)
            )

        if order_items:
            OrderItem.objects.bulk_create(order_items)

        order.total_price = total_price

        return order

