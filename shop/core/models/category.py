from django.db import models


class Category(models.Model):
    """Book Category model"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    class Meta:
        app_label = 'core'
        db_table = 'core_category'

    def __str__(self):
        return self.name
