from django.db import models


class Warehouse(models.Model):
    """Warehouse model for storage locations"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    capacity = models.IntegerField()

    class Meta:
        app_label = 'core'
        db_table = 'core_warehouse'

    def __str__(self):
        return self.name


class Inventory(models.Model):
    """Inventory model for warehouse stock"""
    id = models.AutoField(primary_key=True)
    book = models.OneToOneField('Book', on_delete=models.CASCADE, related_name='inventory')
    quantity_available = models.IntegerField()
    warehouse = models.ForeignKey(Warehouse, on_delete=models.SET_NULL, null=True, blank=True, related_name='inventories')

    class Meta:
        app_label = 'core'
        db_table = 'core_inventory'

    def __str__(self):
        return f"Inventory for {self.book.title}"


class StockInBook(models.Model):
    """Stock In Book model for tracking stock movements"""
    id = models.AutoField(primary_key=True)
    book = models.ForeignKey('Book', on_delete=models.CASCADE, related_name='stock_in_records')
    quantity = models.IntegerField()
    import_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        app_label = 'core'
        db_table = 'core_stock_in_book'

    def __str__(self):
        return f"Stock In: {self.book.title}"


class InventoryStat(models.Model):
    """Inventory Statistics model"""
    id = models.AutoField(primary_key=True)
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    stock_quantity = models.IntegerField()
    total = models.IntegerField()

    class Meta:
        app_label = 'core'
        db_table = 'core_inventory_stat'

    def __str__(self):
        return f"Inventory Stat: {self.book.title}"
