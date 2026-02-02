from django.db import models


class Author(models.Model):
    """Author model representing book authors"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    bio = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'core'
        db_table = 'core_author'

    def __str__(self):
        return self.name
