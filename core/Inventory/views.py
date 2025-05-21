from rest_framework.generics import (
    CreateAPIView, ListAPIView, RetrieveAPIView,
    UpdateAPIView, DestroyAPIView
)
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
from .permissions import IsManager, IsAdminOrManager

# --- CATEGORY VIEWS ---
class CategoryCreateView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryWriteSerializer
    permission_classes = [IsAuthenticated, IsManager]

class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryReadSerializer
    permission_classes = [IsAuthenticated]

class CategoryDetailView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryReadSerializer
    permission_classes = [IsAuthenticated]

class CategoryUpdateView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryWriteSerializer
    permission_classes = [IsAuthenticated, IsManager]

class CategoryDeleteView(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryWriteSerializer
    permission_classes = [IsAuthenticated, IsManager]

# --- PRODUCT VIEWS ---
class ProductCreateView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductWriteSerializer
    permission_classes = [IsAuthenticated, IsManager]

class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductReadSerializer
    permission_classes = [IsAuthenticated]

class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductReadSerializer
    permission_classes = [IsAuthenticated]

class ProductUpdateView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductWriteSerializer
    permission_classes = [IsAuthenticated, IsManager]

class ProductDeleteView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductWriteSerializer
    permission_classes = [IsAuthenticated, IsManager]

# --- SIMILAR PATTERN FOR OTHER MODELS ---
class WarehouseViewSet(ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseWriteSerializer
    permission_classes = [IsAuthenticated, IsAdminOrManager]

class SupplierViewSet(ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierWriteSerializer
    permission_classes = [IsAuthenticated, IsAdminOrManager]

class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerWriteSerializer
    permission_classes = [IsAuthenticated, IsAdminOrManager]

class SalesOrderViewSet(ModelViewSet):
    queryset = SalesOrder.objects.all()
    serializer_class = SalesOrderWriteSerializer
    permission_classes = [IsAuthenticated]

class SalesOrderItemViewSet(ModelViewSet):
    queryset = SalesOrderItem.objects.all()
    serializer_class = SalesOrderItemWriteSerializer
    permission_classes = [IsAuthenticated]

class PurchaseOrderViewSet(ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderWriteSerializer
    permission_classes = [IsAuthenticated]

class PurchaseOrderItemViewSet(ModelViewSet):
    queryset = PurchaseOrderItem.objects.all()
    serializer_class = PurchaseOrderItemWriteSerializer
    permission_classes = [IsAuthenticated]

class BatchViewSet(ModelViewSet):
    queryset = Batch.objects.all()
    serializer_class = BatchWriteSerializer
    permission_classes = [IsAuthenticated]

class StockInViewSet(ModelViewSet):
    queryset = StockIn.objects.all()
    serializer_class = StockInWriteSerializer
    permission_classes = [IsAuthenticated]

class StockOutViewSet(ModelViewSet):
    queryset = StockOut.objects.all()
    serializer_class = StockOutWriteSerializer
    permission_classes = [IsAuthenticated]

class InventoryViewSet(ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventoryWriteSerializer
    permission_classes = [IsAuthenticated]

class AuditLogViewSet(ModelViewSet):
    queryset = AuditLog.objects.all()
    serializer_class = AuditLogWriteSerializer
    permission_classes = [IsAuthenticated]
