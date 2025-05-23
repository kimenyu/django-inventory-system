from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import StockIn, StockOut, Inventory

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
