from django.urls import path
from .views import *

urlpatterns = [
    # Categories
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/create/', CategoryCreateView.as_view(), name='category-create'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('categories/<int:pk>/update/', CategoryUpdateView.as_view(), name='category-update'),
    path('categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category-delete'),

    # Products
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/create/', ProductCreateView.as_view(), name='product-create'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product-update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product-delete'),

    # Warehouses
    path('warehouses/', WarehouseListView.as_view(), name='warehouse-list'),
    path('warehouses/create/', WarehouseCreateView.as_view(), name='warehouse-create'),
    path('warehouses/<int:pk>/', WarehouseDetailView.as_view(), name='warehouse-detail'),
    path('warehouses/<int:pk>/update/', WarehouseUpdateView.as_view(), name='warehouse-update'),
    path('warehouses/<int:pk>/delete/', WarehouseDeleteView.as_view(), name='warehouse-delete'),

    # Suppliers
    path('suppliers/', SupplierListView.as_view(), name='supplier-list'),
    path('suppliers/create/', SupplierCreateView.as_view(), name='supplier-create'),
    path('suppliers/<int:pk>/', SupplierDetailView.as_view(), name='supplier-detail'),
    path('suppliers/<int:pk>/update/', SupplierUpdateView.as_view(), name='supplier-update'),
    path('suppliers/<int:pk>/delete/', SupplierDeleteView.as_view(), name='supplier-delete'),

    # Customers
    path('customers/', CustomerListView.as_view(), name='customer-list'),
    path('customers/create/', CustomerCreateView.as_view(), name='customer-create'),
    path('customers/<int:pk>/', CustomerDetailView.as_view(), name='customer-detail'),
    path('customers/<int:pk>/update/', CustomerUpdateView.as_view(), name='customer-update'),
    path('customers/<int:pk>/delete/', CustomerDeleteView.as_view(), name='customer-delete'),

    # Purchase Orders
    path('purchase-orders/', PurchaseOrderListView.as_view(), name='purchaseorder-list'),
    path('purchase-orders/create/', PurchaseOrderCreateView.as_view(), name='purchaseorder-create'),
    path('purchase-orders/<int:pk>/', PurchaseOrderDetailView.as_view(), name='purchaseorder-detail'),
    path('purchase-orders/<int:pk>/update/', PurchaseOrderUpdateView.as_view(), name='purchaseorder-update'),
    path('purchase-orders/<int:pk>/delete/', PurchaseOrderDeleteView.as_view(), name='purchaseorder-delete'),

    # Purchase Order Items
    path('purchase-order-items/', PurchaseOrderItemListView.as_view(), name='purchaseorderitem-list'),
    path('purchase-order-items/create/', PurchaseOrderItemCreateView.as_view(), name='purchaseorderitem-create'),
    path('purchase-order-items/<int:pk>/', PurchaseOrderItemDetailView.as_view(), name='purchaseorderitem-detail'),
    path('purchase-order-items/<int:pk>/update/', PurchaseOrderItemUpdateView.as_view(), name='purchaseorderitem-update'),
    path('purchase-order-items/<int:pk>/delete/', PurchaseOrderItemDeleteView.as_view(), name='purchaseorderitem-delete'),

    # Sales Orders
    path('sales-orders/', SalesOrderListView.as_view(), name='salesorder-list'),
    path('sales-orders/create/', SalesOrderCreateView.as_view(), name='salesorder-create'),
    path('sales-orders/<int:pk>/', SalesOrderDetailView.as_view(), name='salesorder-detail'),
    path('sales-orders/<int:pk>/update/', SalesOrderUpdateView.as_view(), name='salesorder-update'),
    path('sales-orders/<int:pk>/delete/', SalesOrderDeleteView.as_view(), name='salesorder-delete'),

    # Sales Order Items
    path('sales-order-items/', SalesOrderItemListView.as_view(), name='salesorderitem-list'),
    path('sales-order-items/create/', SalesOrderItemCreateView.as_view(), name='salesorderitem-create'),
    path('sales-order-items/<int:pk>/', SalesOrderItemDetailView.as_view(), name='salesorderitem-detail'),
    path('sales-order-items/<int:pk>/update/', SalesOrderItemUpdateView.as_view(), name='salesorderitem-update'),
    path('sales-order-items/<int:pk>/delete/', SalesOrderItemDeleteView.as_view(), name='salesorderitem-delete'),

    # Batches
    path('batches/', BatchListView.as_view(), name='batch-list'),
    path('batches/create/', BatchCreateView.as_view(), name='batch-create'),
    path('batches/<int:pk>/', BatchDetailView.as_view(), name='batch-detail'),
    path('batches/<int:pk>/update/', BatchUpdateView.as_view(), name='batch-update'),
    path('batches/<int:pk>/delete/', BatchDeleteView.as_view(), name='batch-delete'),

    # Stock In
    path('stock-in/', StockInListView.as_view(), name='stockin-list'),
    path('stock-in/create/', StockInCreateView.as_view(), name='stockin-create'),
    path('stock-in/<int:pk>/', StockInDetailView.as_view(), name='stockin-detail'),
    path('stock-in/<int:pk>/update/', StockInUpdateView.as_view(), name='stockin-update'),
    path('stock-in/<int:pk>/delete/', StockInDeleteView.as_view(), name='stockin-delete'),

    # Stock Out
    path('stock-out/', StockOutListView.as_view(), name='stockout-list'),
    path('stock-out/create/', StockOutCreateView.as_view(), name='stockout-create'),
    path('stock-out/<int:pk>/', StockOutDetailView.as_view(), name='stockout-detail'),
    path('stock-out/<int:pk>/update/', StockOutUpdateView.as_view(), name='stockout-update'),
    path('stock-out/<int:pk>/delete/', StockOutDeleteView.as_view(), name='stockout-delete'),

    # Inventory
    path('inventory/', InventoryListView.as_view(), name='inventory-list'),
    path('inventory/create/', InventoryCreateView.as_view(), name='inventory-create'),
    path('inventory/<int:pk>/', InventoryDetailView.as_view(), name='inventory-detail'),
    path('inventory/<int:pk>/update/', InventoryUpdateView.as_view(), name='inventory-update'),
    path('inventory/<int:pk>/delete/', InventoryDeleteView.as_view(), name='inventory-delete'),

    # Audit Logs
    path('audit-logs/', AuditLogListView.as_view(), name='auditlog-list'),
    path('audit-logs/create/', AuditLogCreateView.as_view(), name='auditlog-create'),
    path('audit-logs/<int:pk>/', AuditLogDetailView.as_view(), name='auditlog-detail'),
    # path('audit-logs/<int:pk>/update/', AuditLogUpdateView.as_view(), name='auditlog-update'),
    # path('audit-logs/<int:pk>/delete/', AuditLogDeleteView.as_view(), name='auditlog-delete'),

    #stock transfer
    path('stock-transfers/', StockTransferListView.as_view(), name='stocktransfer-list'),
    path('stock-transfers/create/', StockTransferCreateView.as_view(), name='stocktransfer-create'),
    path('stock-transfers/<int:pk>/status/', StockTransferStatusUpdateView.as_view(), name='stocktransfer-status-update'),
    path('stock-transfers/stats/', TransferStatsView.as_view(), name='stocktransfer-stats'),


]
