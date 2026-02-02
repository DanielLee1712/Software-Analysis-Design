from core.models.category import Category


class CategoryDAO:
    """Data Access Object for Category model"""

    @staticmethod
    def get_all_categories():
        """Get all categories"""
        return Category.objects.all()

    @staticmethod
    def get_category_by_id(category_id):
        """Get category by ID"""
        try:
            return Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            return None

    @staticmethod
    def create_category(name, description=""):
        """Create a new category"""
        category = Category(name=name, description=description)
        category.save()
        return category

    @staticmethod
    def update_category(category_id, **kwargs):
        """Update category details"""
        try:
            category = Category.objects.get(id=category_id)
            for key, value in kwargs.items():
                if hasattr(category, key):
                    setattr(category, key, value)
            category.save()
            return category
        except Category.DoesNotExist:
            return None

    @staticmethod
    def delete_category(category_id):
        """Delete a category"""
        try:
            category = Category.objects.get(id=category_id)
            category.delete()
            return True
        except Category.DoesNotExist:
            return False
