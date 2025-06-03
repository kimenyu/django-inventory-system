from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import StockIn, StockOut, Inventory, StockTransfer, AuditLog
from django.core.mail import send_mail
from accounts.models import CustomUser  # Import your custom user model

@receiver(post_save, sender=StockIn)
def update_inventory_on_stockin(sender, instance, created, **kwargs):
    if created:
        inventory, _ = Inventory.objects.get_or_create(
            product=instance.product,
            warehouse=instance.warehouse,
            batch=instance.batch,
            defaults={'quantity': 0}
        )
        inventory.quantity += instance.quantity
        inventory.save()

@receiver(post_save, sender=StockOut)
def update_inventory_on_stockout(sender, instance, created, **kwargs):
    if created:
        try:
            inventory = Inventory.objects.get(
                product=instance.product,
                warehouse=instance.warehouse,
                batch=instance.batch
            )
            inventory.quantity -= instance.quantity
            inventory.save()
        except Inventory.DoesNotExist:
            pass



@receiver(post_save, sender=Inventory)
def inventory_threshold_alert(sender, instance, **kwargs):
    status = instance.check_thresholds()

    if status == "low":
        subject = f"Low Stock Alert: {instance.product.name}"
        message = f"The stock for {instance.product.name} is critically low at warehouse {instance.warehouse.name}. Current quantity: {instance.quantity}"
    elif status == "high":
        subject = f"Overstock Alert: {instance.product.name}"
        message = f"The stock for {instance.product.name} has exceeded the max threshold. Quantity: {instance.quantity}"
    elif status == "reorder":
        subject = f"Reorder Notice: {instance.product.name}"
        message = f"The stock for {instance.product.name} is below reorder level. Current quantity: {instance.quantity}"
    else:
        return

    # Get all admin and manager users
    recipients = CustomUser.objects.filter(role__in=["admin", "manager"]).values_list("email", flat=True)

    if recipients:
        send_mail(
            subject,
            message,
            'njorogekimenyu@gmail.com',
            list(recipients),
            fail_silently=False,
        )


@receiver(post_save, sender=StockTransfer)
def log_stock_transfer(sender, instance, created, **kwargs):
    if created:
        status_note = "Created"
    elif instance.status == "COMPLETED":
        status_note = "Completed"
    elif instance.status == "CANCELED":
        status_note = "Canceled"
    else:
        status_note = f"Updated to {instance.status}"

    AuditLog.objects.create(
        user=instance.created_by,
        action=f"{status_note} stock transfer of {instance.quantity} '{instance.product}' "
               f"from '{instance.source_warehouse}' to '{instance.destination_warehouse}'"
    )

@receiver(post_save, sender=StockTransfer)
def handle_inventory_transfer(sender, instance, created, **kwargs):
    if not created or instance.status != 'COMPLETED':
        return

    # Deduct from source warehouse
    source_inventory, _ = Inventory.objects.get_or_create(
        product=instance.product,
        warehouse=instance.source_warehouse,
        batch=instance.batch,
        defaults={'quantity': 0}
    )
    source_inventory.quantity = max(source_inventory.quantity - instance.quantity, 0)
    source_inventory.save()

    # Add to destination warehouse
    dest_inventory, _ = Inventory.objects.get_or_create(
        product=instance.product,
        warehouse=instance.destination_warehouse,
        batch=instance.batch,
        defaults={'quantity': 0}
    )
    dest_inventory.quantity += instance.quantity
    dest_inventory.save()
