from django.db import models


class Book(models.Model):
    """Book model representing products in the catalog"""
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True, blank=True)
    publisher = models.ForeignKey('Publisher', on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True, related_name='books')
    translator = models.ForeignKey('Translator', on_delete=models.SET_NULL, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    description = models.TextField(blank=True, null=True)
    language = models.CharField(max_length=50, default='en')
    isbn = models.CharField(max_length=20, unique=True, blank=True, null=True)
    publication_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'core'
        db_table = 'core_book'

    def __str__(self):
        author_name = self.author.name if self.author else 'Unknown'
        return f"{self.title} by {author_name}"
