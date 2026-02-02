from django.db import models


class RevenueReport(models.Model):
    """Revenue Report model for business analytics"""
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=50)
    total = models.DecimalField(max_digits=12, decimal_places=2)
    desc = models.TextField(blank=True, null=True)
    total_customer = models.IntegerField()

    class Meta:
        app_label = 'core'
        db_table = 'core_revenue_report'

    def __str__(self):
        return f"Revenue Report: {self.type}"


class RatingStat(models.Model):
    """Rating Statistics model"""
    id = models.AutoField(primary_key=True)
    book = models.ForeignKey('Book', on_delete=models.CASCADE, related_name='rating_stats')
    type = models.CharField(max_length=50)
    total = models.IntegerField()
    host_customer = models.IntegerField()

    class Meta:
        app_label = 'core'
        db_table = 'core_rating_stat'

    def __str__(self):
        return f"Rating Stat for {self.book.title}"
