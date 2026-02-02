from django.db import models


class MembershipLevel(models.Model):
    """Membership Level model for customer tiers"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    discount_rate = models.DecimalField(max_digits=5, decimal_places=2)
    required_points = models.IntegerField()
    benefit_description = models.TextField(blank=True, null=True)

    class Meta:
        app_label = 'core'
        db_table = 'core_membership_level'

    def __str__(self):
        return self.name


class PointHistory(models.Model):
    """Point History model for tracking customer loyalty points"""
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE, related_name='point_history')
    points = models.IntegerField()
    customer_id_str = models.CharField(max_length=255)

    class Meta:
        app_label = 'core'
        db_table = 'core_point_history'

    def __str__(self):
        return f"Points for {self.customer.name}: {self.points}"


class CustomerAnalytic(models.Model):
    """Customer Analytics model for tracking customer metrics"""
    id = models.AutoField(primary_key=True)
    customer = models.OneToOneField('Customer', on_delete=models.CASCADE, related_name='analytics')
    total_spent = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    favorite_genre = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        app_label = 'core'
        db_table = 'core_customer_analytic'

    def __str__(self):
        return f"Analytics for {self.customer.name}"
