from django.db import models


class OrderHistory(models.Model):
    """OrderHistory model tracking customer orders"""
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE, related_name='order_history')
    order = models.ForeignKey('Order', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        app_label = 'core'
        db_table = 'core_order_history'

    def __str__(self):
        return f"Order history for {self.customer.name}"


class Order(models.Model):
    """Order model representing customer orders"""
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]
    
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE, related_name='orders')
    address = models.ForeignKey('Address', on_delete=models.SET_NULL, null=True, blank=True)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    total_price = models.DecimalField(max_digits=12, decimal_places=2)
    changed_at = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'core'
        db_table = 'core_order'

    def __str__(self):
        return f"Order #{self.id} - {self.customer.name}"
