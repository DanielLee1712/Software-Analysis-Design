from django.db import models


class Voucher(models.Model):
    """Voucher model for discount vouchers"""
    id = models.AutoField(primary_key=True)
    voucher_code = models.CharField(max_length=255, unique=True)
    max_usage = models.IntegerField()
    current_usage = models.IntegerField(default=0)
    discount_value = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        app_label = 'core'
        db_table = 'core_voucher'

    def __str__(self):
        return self.voucher_code
