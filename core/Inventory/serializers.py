from rest_framework import serializers
from .models import Category, Product, Warehouse, Batch, SalesOrder, SalesOrderItem, StockIn, StockOut, Supplier, Customer, PurchaseOrder, PurchaseOrderItem, Inventory, AuditLog

class ProductWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['sku', 'name', 'description', 'price', 'unit', 'category']

    def validate_price(self, value: float) -> float:
        if value < 0:
            raise serializers.ValidationError("Price cannot be less than 0")
        return value


class ProductReadSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = ['sku', 'name', 'description', 'price', 'unit', 'category']


class CategoryWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'description']


class CategoryReadSerializer(serializers.ModelSerializer):
    products = ProductReadSerializer(source='product_set', many=True)

    class Meta:
        model = Category
        fields = ['name', 'description', 'products']


class BatchWriteSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    class Meta:
        model = Batch
        fields = ['batch_number', 'expiry_date', 'product']


class BatchReadSerializer(serializers.ModelSerializer):
    product = ProductReadSerializer()

    class Meta:
        model = Batch
        fields = ['batch_number', 'expiry_date', 'product']

class WarehouseWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = ['name', 'location']

class SupplierWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['name', 'contact_info']

class PurchaseOrderItemReadSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['order', 'product', 'quantity', 'warehouse', 'batch']

class PurchaseOrderReadSerializer(serializers.ModelSerializer):
    supplier = serializers.StringRelatedField()
    purchase_order_item = PurchaseOrderItemReadSerializer(many=True)
    class Meta:
        fields = ['supplier', 'date', 'status']

class SupplierReadSerializer(serializers.ModelSerializer):
    purchase_order = PurchaseOrderReadSerializer(many=True)
    class Meta:
        model = Supplier
        fields = ['name', 'contact_info', 'purchase_order']

class CustomerWriteSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['name', 'contact_info']

class PurchaseOrderWriteSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['supplier', 'date', 'status']


class PurchaseOrderItemWriteSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['order', 'product', 'quantity', 'warehouse', 'batch']

    def validate_quantity(self, value: float) -> float:
        if value <= 0:
            raise serializers.ValidationError("Quantity must be greater than 0")
        return value

