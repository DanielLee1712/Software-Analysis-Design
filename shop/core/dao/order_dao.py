from core.models.order import Order


class OrderDAO:
    """Data Access Object for Order model"""

    @staticmethod
    def get_all_orders():
        """Get all orders"""
        return Order.objects.all()

    @staticmethod
    def get_order_by_id(order_id):
        """Get order by ID"""
        try:
            return Order.objects.get(id=order_id)
        except Order.DoesNotExist:
            return None

    @staticmethod
    def get_orders_by_customer(customer_id):
        """Get all orders by a customer"""
        return Order.objects.filter(customer_id=customer_id)

    @staticmethod
    def create_order(customer_id, address_id=None, total_price=0):
        """Create a new order"""
        order = Order(
            customer_id=customer_id,
            address_id=address_id,
            total_price=total_price
        )
        order.save()
        return order

    @staticmethod
    def update_order_status(order_id, status):
        """Update order status"""
        try:
            order = Order.objects.get(id=order_id)
            order.status = status
            order.save()
            return order
        except Order.DoesNotExist:
            return None

    @staticmethod
    def delete_order(order_id):
        """Delete an order"""
        try:
            order = Order.objects.get(id=order_id)
            order.delete()
            return True
        except Order.DoesNotExist:
            return False

    @staticmethod
    def get_orders_by_status(status):
        """Get orders by status"""
        return Order.objects.filter(status=status)
