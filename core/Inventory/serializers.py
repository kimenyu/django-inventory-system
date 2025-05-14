from rest_framework import serializers
from .models import Category, Product, Warehouse, Batch, SalesOrder, SalesOrderItem, StockIn, StockOut, Supplier, Customer, PurchaseOrder, PurchaseOrderItem, Inventory, AuditLog
from typing import Any, Dict, List



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['sku', 'name', 'description', 'price', 'unit']

    def validate_price(self, value: float) -> float:
        if value < 0:
            raise serializers.ValidationError("Price cannot be less than 0")
        return value


class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Category
        fields = ['name', 'description', 'products']

    def create(self, validated_data: Dict[str, Any]) -> Category:
        products_data: List[Dict[str, Any]] = validated_data.pop('products')
        category = Category.objects.create(**validated_data)
        for product_data in products_data:
            Product.objects.create(category=category, **product_data)
        return category

    def update(self, instance: Category, validated_data: Dict[str, Any]) -> Category:
        products_data: List[Dict[str, Any]] = validated_data.pop('products', [])

        # Update category fields
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.save()

        # Delete existing products and recreate
        instance.product_set.all().delete()
        for product_data in products_data:
            Product.objects.create(category=instance, **product_data)

        return instance
