from rest_framework import serializers
from .models import Category, Product, Warehouse, Batch, SalesOrder, SalesOrderItem, StockIn, StockOut, Supplier, Customer, PurchaseOrder, PurchaseOrderItem, Inventory, AuditLog
from accounts.models import CustomUser

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

class StockInReadSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['product', 'quantity', 'warehouse', 'batch', 'purchase_order', 'date']

class StockOutReadSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['product', 'quantity', 'warehouse', 'batch', 'sales_order', 'date']

class WarehouseReadSerializer(serializers.ModelSerializer):
    stock_in = StockInReadSerializer(many=True)
    stock_out = StockOutReadSerializer(many=True)
    class Meta:
        fields = ['name', 'location', 'stock_in', 'stock_out']

class SupplierWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['name', 'contact_info']

class PurchaseOrderItemReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrderItem
        fields = ['order', 'product', 'quantity', 'warehouse', 'batch']

class PurchaseOrderReadSerializer(serializers.ModelSerializer):
    supplier = serializers.StringRelatedField()
    purchase_order_item = PurchaseOrderItemReadSerializer(many=True, source='items')
    class Meta:
        model = PurchaseOrder
        fields = ['supplier', 'purchase_order_item', 'date', 'status']

class SupplierReadSerializer(serializers.ModelSerializer):
    purchase_order = PurchaseOrderReadSerializer(many=True, source='purchaseorder_set')

    class Meta:
        model = Supplier
        fields = ['name', 'contact_info', 'purchase_order']

class CustomerWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['name', 'contact_info']

class SalesOrderItemsReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesOrderItem
        fields = ['order', 'quantity', 'warehouse', 'batch', 'product', 'date']

class SalesOrderReadSerializer(serializers.ModelSerializer):
    sales_order_items = SalesOrderItemsReadSerializer(many=True, source='items')

    class Meta:
        model = SalesOrder
        fields = ['customer', 'date', 'status', 'sales_order_items']
        read_only_fields = ['date']

class CustomerReadSerializer(serializers.ModelSerializer):
    sales_orders = SalesOrderReadSerializer(many=True, source="salesorder_set")
    class Meta:
        model = Customer
        fields = ['name', 'contact_info', 'sales_orders']

class PurchaseOrderWriteSerializer(serializers.ModelSerializer):
    supplier = serializers.PrimaryKeyRelatedField(queryset=Supplier.objects.all())

    class Meta:
        model = PurchaseOrder
        fields = ['supplier', 'date', 'status']


class PurchaseOrderItemWriteSerializer(serializers.ModelSerializer):
    order = serializers.PrimaryKeyRelatedField(queryset=PurchaseOrder.objects.all())
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    warehouse = serializers.PrimaryKeyRelatedField(queryset=Warehouse.objects.all())
    batch = serializers.PrimaryKeyRelatedField(queryset=Batch.objects.all())

    class Meta:
        model = PurchaseOrderItem
        fields = ['order', 'product', 'quantity', 'warehouse', 'batch']


class SalesOrderWriteSerializer(serializers.ModelSerializer):
    customer = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all())

    class Meta:
        model = SalesOrder
        fields = ['customer', 'date', 'status']


class SalesOrderItemWriteSerializer(serializers.ModelSerializer):
    order = serializers.PrimaryKeyRelatedField(queryset=SalesOrder.objects.all())
    warehouse = serializers.PrimaryKeyRelatedField(queryset=Warehouse.objects.all())
    batch = serializers.PrimaryKeyRelatedField(queryset=Batch.objects.all())
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    class Meta:
        model = SalesOrderItem
        fields = ['order', 'quantity', 'warehouse', 'batch', 'product', 'date']

class StockInWriteSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    warehouse = serializers.PrimaryKeyRelatedField(queryset=Warehouse.objects.all())
    batch = serializers.PrimaryKeyRelatedField(queryset=Batch.objects.all())
    purchase_order = serializers.PrimaryKeyRelatedField(queryset=PurchaseOrder.objects.all())

    class Meta:
        model = StockIn
        fields = ['product', 'quantity', 'warehouse', 'batch', 'purchase_order', 'date']


class StockOutWriteSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    warehouse = serializers.PrimaryKeyRelatedField(queryset=Warehouse.objects.all())
    batch = serializers.PrimaryKeyRelatedField(queryset=Batch.objects.all())
    sales_order = serializers.PrimaryKeyRelatedField(queryset=SalesOrder.objects.all())

    class Meta:
        model = StockOut
        fields = ['product', 'quantity', 'warehouse', 'batch', 'sales_order', 'date']

class InventoryWriteSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    warehouse = serializers.PrimaryKeyRelatedField(queryset=Warehouse.objects.all())
    batch = serializers.PrimaryKeyRelatedField(queryset=Batch.objects.all())

    class Meta:
        model = Inventory
        fields = ['product', 'warehouse', 'batch', 'quantity']

class InventoryReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ['product', 'warehouse', 'batch', 'quantity']

class AuditLogWriteSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    class Meta:
        model = AuditLog
        fields = ['user', 'action', 'timestamp']