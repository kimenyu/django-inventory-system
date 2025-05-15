from django.db import models
from accounts.models import CustomUser

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Warehouse(models.Model):
    name = models.CharField(max_length=100)
    location = models.TextField()

    def __str__(self):
        return self.name

class Product(models.Model):
    sku = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=50)  # e.g., kg, pcs

    def __str__(self):
        return f"{self.name} ({self.sku})"

class Batch(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    batch_number = models.CharField(max_length=100)
    expiry_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.product.name} - Batch {self.batch_number}"

class Supplier(models.Model):
    name = models.CharField(max_length=200)
    contact_info = models.TextField()

    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=200)
    contact_info = models.TextField()

    def __str__(self):
        return self.name

class PurchaseOrder(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[('Pending', 'Pending'), ('Received', 'Received')])

    def __str__(self):
        return f"PO-{self.id} from {self.supplier.name}"

class PurchaseOrderItem(models.Model):
    order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    batch = models.ForeignKey(Batch, on_delete=models.SET_NULL, null=True, blank=True)

class SalesOrder(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[('Pending', 'Pending'), ('Delivered', 'Delivered')])

    def __str__(self):
        return f"SO-{self.id} to {self.customer.name}"

class SalesOrderItem(models.Model):
    order = models.ForeignKey(SalesOrder, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    batch = models.ForeignKey(Batch, on_delete=models.SET_NULL, null=True, blank=True)

class StockIn(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    batch = models.ForeignKey(Batch, on_delete=models.SET_NULL, null=True, blank=True)
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField(auto_now_add=True)
        

class StockOut(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    batch = models.ForeignKey(Batch, on_delete=models.SET_NULL, null=True, blank=True)
    sales_order = models.ForeignKey(SalesOrder, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField(auto_now_add=True)

class Inventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    batch = models.ForeignKey(Batch, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=0)

    class Meta:
        unique_together = ('product', 'warehouse', 'batch')


class AuditLog(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    action = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
