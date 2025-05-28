from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import StockIn, StockOut, Inventory
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
            # Optionally raise an error or log
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
            'njorogekimenyu@gmail.com',  # Change to your FROM address
            list(recipients),
            fail_silently=False,
        )
