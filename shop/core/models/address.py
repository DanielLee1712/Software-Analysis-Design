from django.db import models


class Address(models.Model):
    """Address model for customers and suppliers"""
    id = models.AutoField(primary_key=True)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    province = models.CharField(max_length=255)

    class Meta:
        app_label = 'core'
        db_table = 'core_address'

    def __str__(self):
        return f"{self.street}, {self.city}, {self.province}"
