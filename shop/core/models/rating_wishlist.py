from django.db import models


class Rating(models.Model):
    """Rating model for book ratings by customers"""
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE, related_name='ratings')
    book = models.ForeignKey('Book', on_delete=models.CASCADE, related_name='ratings')
    score = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'core'
        db_table = 'core_rating'
        unique_together = ('customer', 'book')

    def __str__(self):
        return f"{self.customer.name} rated {self.book.title}: {self.score}/5"


class Wishlist(models.Model):
    """Wishlist model for customers to save books"""
    id = models.AutoField(primary_key=True)
    customer = models.OneToOneField('Customer', on_delete=models.CASCADE, related_name='wishlist')
    is_public = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'core'
        db_table = 'core_wishlist'

    def __str__(self):
        return f"Wishlist of {self.customer.name}"


class WishlistItem(models.Model):
    """Items in a wishlist"""
    id = models.AutoField(primary_key=True)
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE, related_name='items')
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    added_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'core'
        db_table = 'core_wishlist_item'
        unique_together = ('wishlist', 'book')

    def __str__(self):
        return f"{self.book.title} in {self.wishlist.customer.name}'s wishlist"
