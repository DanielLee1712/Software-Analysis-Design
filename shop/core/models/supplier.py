from django.db import models


class Supplier(models.Model):
    """Supplier model for book suppliers"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    address = models.ForeignKey('Address', on_delete=models.SET_NULL, null=True, blank=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    add_date = models.DateTimeField(auto_now_add=True)
    total_import_price = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    class Meta:
        app_label = 'core'
        db_table = 'core_supplier'

    def __str__(self):
        return self.name
