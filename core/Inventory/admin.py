from django.contrib import admin
from .models import Category, Product, Warehouse, Batch, SalesOrder, SalesOrderItem, StockIn, StockOut, Supplier, Customer, PurchaseOrder, PurchaseOrderItem, Inventory, AuditLog


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Warehouse)
admin.site.register(Batch)
admin.site.register(SalesOrder)
admin.site.register(SalesOrderItem)
admin.site.register(StockIn)
admin.site.register(StockOut)
admin.site.register(Supplier)
admin.site.register(Customer)
admin.site.register(PurchaseOrder)
admin.site.register(PurchaseOrderItem)
admin.site.register(Inventory)
admin.site.register(AuditLog)
