from django.db import models


class BookSeries(models.Model):
    """Book Series model for grouping related books"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    books = models.ManyToManyField('Book', related_name='series')

    class Meta:
        app_label = 'core'
        db_table = 'core_book_series'

    def __str__(self):
        return self.name
