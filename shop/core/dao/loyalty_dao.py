from core.models.loyalty import MembershipLevel, PointHistory


class MembershipDAO:
    """Data Access Object for Membership model"""

    @staticmethod
    def get_all_levels():
        """Get all membership levels"""
        return MembershipLevel.objects.all()

    @staticmethod
    def get_level_by_id(level_id):
        """Get membership level by ID"""
        try:
            return MembershipLevel.objects.get(id=level_id)
        except MembershipLevel.DoesNotExist:
            return None

    @staticmethod
    def create_level(name, discount_rate, required_points):
        """Create a new membership level"""
        level = MembershipLevel(
            name=name,
            discount_rate=discount_rate,
            required_points=required_points
        )
        level.save()
        return level

    @staticmethod
    def get_level_by_points(points):
        """Get membership level based on points"""
        return MembershipLevel.objects.filter(
            required_points__lte=points
        ).order_by('-required_points').first()


class PointHistoryDAO:
    """Data Access Object for PointHistory model"""

    @staticmethod
    def get_points_by_customer(customer_id):
        """Get all point history for a customer"""
        return PointHistory.objects.filter(customer_id=customer_id)

    @staticmethod
    def add_points(customer_id, points):
        """Add points to customer's loyalty account"""
        history = PointHistory(customer_id=customer_id, points=points)
        history.save()
        return history

    @staticmethod
    def get_total_points(customer_id):
        """Get total loyalty points for a customer"""
        from django.db.models import Sum
        total = PointHistory.objects.filter(customer_id=customer_id).aggregate(
            Sum('points')
        )
        return total['points__sum'] or 0
