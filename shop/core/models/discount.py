from django.db import models


class Discount(models.Model):
    """Discount model for managing discounts"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    discount_rate = models.DecimalField(max_digits=5, decimal_places=2)
    method_name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    class Meta:
        app_label = 'core'
        db_table = 'core_discount'

    def __str__(self):
        return f"{self.name} - {self.discount_rate}%"
