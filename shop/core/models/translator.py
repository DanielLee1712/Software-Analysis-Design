from django.db import models


class Translator(models.Model):
    """Translator model for book translations"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    language = models.CharField(max_length=50)
    bio = models.TextField(blank=True, null=True)

    class Meta:
        app_label = 'core'
        db_table = 'core_translator'

    def __str__(self):
        return self.name
