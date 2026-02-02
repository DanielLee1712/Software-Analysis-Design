from core.models.warehouse import Inventory, Warehouse


class InventoryDAO:
    """Data Access Object for Inventory model"""

    @staticmethod
    def get_inventory_by_book(book_id):
        """Get inventory for a book"""
        try:
            return Inventory.objects.get(book_id=book_id)
        except Inventory.DoesNotExist:
            return None

    @staticmethod
    def update_inventory_quantity(book_id, quantity):
        """Update inventory quantity for a book"""
        try:
            inventory = Inventory.objects.get(book_id=book_id)
            inventory.quantity_available = quantity
            inventory.save()
            return inventory
        except Inventory.DoesNotExist:
            return None

    @staticmethod
    def increase_inventory(book_id, amount):
        """Increase inventory quantity"""
        try:
            inventory = Inventory.objects.get(book_id=book_id)
            inventory.quantity_available += amount
            inventory.save()
            return inventory
        except Inventory.DoesNotExist:
            return None

    @staticmethod
    def decrease_inventory(book_id, amount):
        """Decrease inventory quantity"""
        try:
            inventory = Inventory.objects.get(book_id=book_id)
            if inventory.quantity_available >= amount:
                inventory.quantity_available -= amount
                inventory.save()
                return inventory
            return None
        except Inventory.DoesNotExist:
            return None

    @staticmethod
    def get_low_stock_books(threshold=10):
        """Get books with low stock"""
        return Inventory.objects.filter(quantity_available__lt=threshold)


class WarehouseDAO:
    """Data Access Object for Warehouse model"""

    @staticmethod
    def get_all_warehouses():
        """Get all warehouses"""
        return Warehouse.objects.all()

    @staticmethod
    def get_warehouse_by_id(warehouse_id):
        """Get warehouse by ID"""
        try:
            return Warehouse.objects.get(id=warehouse_id)
        except Warehouse.DoesNotExist:
            return None

    @staticmethod
    def create_warehouse(name, location, capacity):
        """Create a new warehouse"""
        warehouse = Warehouse(name=name, location=location, capacity=capacity)
        warehouse.save()
        return warehouse

    @staticmethod
    def get_warehouse_inventory(warehouse_id):
        """Get all inventory in a warehouse"""
        return Inventory.objects.filter(warehouse_id=warehouse_id)
