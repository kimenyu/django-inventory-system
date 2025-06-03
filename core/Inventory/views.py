from rest_framework.generics import (
    CreateAPIView, ListAPIView, RetrieveAPIView,
    UpdateAPIView, DestroyAPIView
)
from rest_framework.generics import UpdateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
from .permissions import IsManager, IsAdminOrManager
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.timezone import now, timedelta

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

# --- WAREHOUSE VIEWS ---
class WarehouseCreateView(CreateAPIView):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseWriteSerializer
    permission_classes = [IsAuthenticated, IsAdminOrManager]
    
class WarehouseListView(ListAPIView):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseWriteSerializer
    permission_classes = [IsAuthenticated]

class WarehouseDetailView(RetrieveAPIView):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseWriteSerializer
    permission_classes = [IsAuthenticated]

class WarehouseUpdateView(UpdateAPIView):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseWriteSerializer
    permission_classes = [IsAuthenticated, IsAdminOrManager]
class WarehouseDeleteView(DestroyAPIView):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseWriteSerializer
    permission_classes = [IsAuthenticated, IsAdminOrManager]

class SupplierCreateView(CreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierWriteSerializer
    permission_classes = [IsAuthenticated, IsAdminOrManager]
class SupplierListView(ListAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierReadSerializer
    permission_classes = [IsAuthenticated]

class SupplierDetailView(RetrieveAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierReadSerializer
    permission_classes = [IsAuthenticated]

class SupplierUpdateView(UpdateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierWriteSerializer
    permission_classes = [IsAuthenticated, IsAdminOrManager]
class SupplierDeleteView(DestroyAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierWriteSerializer
    permission_classes = [IsAuthenticated, IsAdminOrManager]
class CustomerCreateView(CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerWriteSerializer
    permission_classes = [IsAuthenticated, IsAdminOrManager]
class CustomerListView(ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerReadSerializer
    permission_classes = [IsAuthenticated]

class CustomerDetailView(RetrieveAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerReadSerializer
    permission_classes = [IsAuthenticated]

class CustomerUpdateView(UpdateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerWriteSerializer
    permission_classes = [IsAuthenticated, IsAdminOrManager]
class CustomerDeleteView(DestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerWriteSerializer
    permission_classes = [IsAuthenticated, IsAdminOrManager]

class SalesOrderCreateView(CreateAPIView):
    queryset = SalesOrder.objects.all()
    serializer_class = SalesOrderWriteSerializer
    permission_classes = [IsAuthenticated]

class SalesOrderListView(ListAPIView):
    queryset = SalesOrder.objects.all()
    serializer_class = SalesOrderReadSerializer
    permission_classes = [IsAuthenticated]

class SalesOrderDetailView(RetrieveAPIView):
    queryset = SalesOrder.objects.all()
    serializer_class = SalesOrderReadSerializer
    permission_classes = [IsAuthenticated]

class SalesOrderUpdateView(UpdateAPIView):
    queryset = SalesOrder.objects.all()
    serializer_class = SalesOrderWriteSerializer
    permission_classes = [IsAuthenticated]

class SalesOrderDeleteView(DestroyAPIView):
    queryset = SalesOrder.objects.all()
    serializer_class = SalesOrderWriteSerializer
    permission_classes = [IsAuthenticated]

class SalesOrderItemCreateView(CreateAPIView):
    queryset = SalesOrderItem.objects.all()
    serializer_class = SalesOrderItemWriteSerializer
    permission_classes = [IsAuthenticated]

class SalesOrderItemListView(ListAPIView):
    queryset = SalesOrderItem.objects.all()
    serializer_class = SalesOrderItemWriteSerializer
    permission_classes = [IsAuthenticated]

class SalesOrderItemDetailView(RetrieveAPIView):
    queryset = SalesOrderItem.objects.all()
    serializer_class = SalesOrderItemWriteSerializer
    permission_classes = [IsAuthenticated]

class SalesOrderItemUpdateView(UpdateAPIView):
    queryset = SalesOrderItem.objects.all()
    serializer_class = SalesOrderItemWriteSerializer
    permission_classes = [IsAuthenticated]

class SalesOrderItemDeleteView(DestroyAPIView):
    queryset = SalesOrderItem.objects.all()
    serializer_class = SalesOrderItemWriteSerializer
    permission_classes = [IsAuthenticated]

class PurchaseOrderCreateView(CreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderWriteSerializer
    permission_classes = [IsAuthenticated]

class PurchaseOrderListView(ListAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderReadSerializer
    permission_classes = [IsAuthenticated]

class PurchaseOrderDetailView(RetrieveAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderReadSerializer
    permission_classes = [IsAuthenticated]

class PurchaseOrderUpdateView(UpdateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderWriteSerializer
    permission_classes = [IsAuthenticated]

class PurchaseOrderDeleteView(DestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderWriteSerializer
    permission_classes = [IsAuthenticated]

class PurchaseOrderItemCreateView(CreateAPIView):
    queryset = PurchaseOrderItem.objects.all()
    serializer_class = PurchaseOrderItemWriteSerializer
    permission_classes = [IsAuthenticated]

class PurchaseOrderItemListView(ListAPIView):
    queryset = PurchaseOrderItem.objects.all()
    serializer_class = PurchaseOrderItemWriteSerializer
    permission_classes = [IsAuthenticated]

class PurchaseOrderItemDetailView(RetrieveAPIView):
    queryset = PurchaseOrderItem.objects.all()
    serializer_class = PurchaseOrderItemWriteSerializer
    permission_classes = [IsAuthenticated]

class PurchaseOrderItemUpdateView(UpdateAPIView):
    queryset = PurchaseOrderItem.objects.all()
    serializer_class = PurchaseOrderItemWriteSerializer
    permission_classes = [IsAuthenticated]

class PurchaseOrderItemDeleteView(DestroyAPIView):
    queryset = PurchaseOrderItem.objects.all()
    serializer_class = PurchaseOrderItemWriteSerializer
    permission_classes = [IsAuthenticated]

class BatchCreateView(CreateAPIView):
    queryset = Batch.objects.all()
    serializer_class = BatchWriteSerializer
    permission_classes = [IsAuthenticated]

class BatchListView(ListAPIView):
    queryset = Batch.objects.all()
    serializer_class = BatchReadSerializer
    permission_classes = [IsAuthenticated]

class BatchDetailView(RetrieveAPIView):
    queryset = Batch.objects.all()
    serializer_class = BatchReadSerializer
    permission_classes = [IsAuthenticated]

class BatchUpdateView(UpdateAPIView):
    queryset = Batch.objects.all()
    serializer_class = BatchWriteSerializer
    permission_classes = [IsAuthenticated]

class BatchDeleteView(DestroyAPIView):
    queryset = Batch.objects.all()
    serializer_class = BatchWriteSerializer
    permission_classes = [IsAuthenticated]


class StockInCreateView(CreateAPIView):
    queryset = StockIn.objects.all()
    serializer_class = StockInWriteSerializer
    permission_classes = [IsAuthenticated]

class StockInListView(ListAPIView):
    queryset = StockIn.objects.all()
    serializer_class = StockInReadSerializer
    permission_classes = [IsAuthenticated]

class StockInDetailView(RetrieveAPIView):
    queryset = StockIn.objects.all()
    serializer_class = StockInReadSerializer
    permission_classes = [IsAuthenticated]

class StockInUpdateView(UpdateAPIView):
    queryset = StockIn.objects.all()
    serializer_class = StockInWriteSerializer
    permission_classes = [IsAuthenticated]

class StockInDeleteView(DestroyAPIView):
    queryset = StockIn.objects.all()
    serializer_class = StockInWriteSerializer
    permission_classes = [IsAuthenticated]


class StockOutCreateView(CreateAPIView):
    queryset = StockOut.objects.all()
    serializer_class = StockOutWriteSerializer
    permission_classes = [IsAuthenticated]

class StockOutListView(ListAPIView):
    queryset = StockOut.objects.all()
    serializer_class = StockOutReadSerializer
    permission_classes = [IsAuthenticated]

class StockOutDetailView(RetrieveAPIView):
    queryset = StockOut.objects.all()
    serializer_class = StockOutReadSerializer
    permission_classes = [IsAuthenticated]

class StockOutUpdateView(UpdateAPIView):
    queryset = StockOut.objects.all()
    serializer_class = StockOutWriteSerializer
    permission_classes = [IsAuthenticated]

class StockOutDeleteView(DestroyAPIView):
    queryset = StockOut.objects.all()
    serializer_class = StockOutWriteSerializer
    permission_classes = [IsAuthenticated]


class InventoryCreateView(CreateAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventoryWriteSerializer
    permission_classes = [IsAuthenticated]

class InventoryListView(ListAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventoryReadSerializer
    permission_classes = [IsAuthenticated]

class InventoryDetailView(RetrieveAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventoryReadSerializer
    permission_classes = [IsAuthenticated]

class InventoryUpdateView(UpdateAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventoryWriteSerializer
    permission_classes = [IsAuthenticated]

class InventoryDeleteView(DestroyAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventoryWriteSerializer
    permission_classes = [IsAuthenticated]


class AuditLogCreateView(CreateAPIView):
    queryset = AuditLog.objects.all()
    serializer_class = AuditLogWriteSerializer
    permission_classes = [IsAuthenticated]

class AuditLogListView(ListAPIView):
    queryset = AuditLog.objects.all()
    serializer_class = AuditLogWriteSerializer
    permission_classes = [IsAuthenticated]

class AuditLogDetailView(RetrieveAPIView):
    queryset = AuditLog.objects.all()
    serializer_class = AuditLogWriteSerializer
    permission_classes = [IsAuthenticated]


class StockTransferCreateView(CreateAPIView):
    queryset = StockTransfer.objects.all()
    serializer_class = StockTransferSerializer
    permission_classes = [IsAdminOrManager]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class StockTransferListView(ListAPIView):
    queryset = StockTransfer.objects.all()
    serializer_class = StockTransferSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'source_warehouse', 'destination_warehouse', 'created_at']

class StockTransferStatusUpdateView(UpdateAPIView):
    queryset = StockTransfer.objects.all()
    serializer_class = StockTransferSerializer
    permission_classes = [IsAdminOrManager]

    def perform_update(self, serializer):
        prev_status = self.get_object().status
        new_instance = serializer.save()

        if prev_status != 'COMPLETED' and new_instance.status == 'COMPLETED':
            # Trigger inventory update manually
            from django.db.models.signals import post_save
            post_save.send(sender=StockTransfer, instance=new_instance, created=False)



class TransferStatsView(APIView):
    def get(self, request):
        today = now().date()
        last_7_days = today - timedelta(days=7)
        last_month = today - timedelta(days=30)

        data = {
            "last_7_days": StockTransfer.objects.filter(created_at__gte=last_7_days).count(),
            "last_30_days": StockTransfer.objects.filter(created_at__gte=last_month).count(),
            "pending": StockTransfer.objects.filter(status="PENDING").count(),
            "completed": StockTransfer.objects.filter(status="COMPLETED").count(),
        }
        return Response(data)
