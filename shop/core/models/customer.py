from django.db import models


class Customer(models.Model):
    """Customer model representing a registered user in the system"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.ForeignKey('Address', on_delete=models.SET_NULL, null=True, blank=True)
    membership_level = models.ForeignKey('MembershipLevel', on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    loyalty_points = models.IntegerField(default=0)

    class Meta:
        app_label = 'core'
        db_table = 'core_customer'

    def __str__(self):
        return f"{self.name} ({self.email})"
