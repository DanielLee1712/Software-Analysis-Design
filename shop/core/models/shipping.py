from django.db import models


class Shipping(models.Model):
    """Shipping model for order delivery"""
    id = models.AutoField(primary_key=True)
    order = models.OneToOneField('Order', on_delete=models.CASCADE, related_name='shipping')
    method_name = models.CharField(max_length=255)
    fee = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        app_label = 'core'
        db_table = 'core_shipping'

    def __str__(self):
        return f"Shipping for Order #{self.order.id}"
