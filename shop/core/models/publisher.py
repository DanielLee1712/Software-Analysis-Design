from django.db import models


class Publisher(models.Model):
    """Publisher model representing book publishers"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        app_label = 'core'
        db_table = 'core_publisher'

    def __str__(self):
        return self.name
