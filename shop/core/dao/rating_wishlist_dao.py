from core.models.rating_wishlist import Rating, Wishlist, WishlistItem


class RatingDAO:
    """Data Access Object for Rating model"""

    @staticmethod
    def get_rating_by_id(rating_id):
        """Get rating by ID"""
        try:
            return Rating.objects.get(id=rating_id)
        except Rating.DoesNotExist:
            return None

    @staticmethod
    def get_ratings_by_book(book_id):
        """Get all ratings for a book"""
        return Rating.objects.filter(book_id=book_id)

    @staticmethod
    def get_ratings_by_customer(customer_id):
        """Get all ratings by a customer"""
        return Rating.objects.filter(customer_id=customer_id)

    @staticmethod
    def create_rating(customer_id, book_id, score):
        """Create a new rating"""
        rating = Rating(customer_id=customer_id, book_id=book_id, score=score)
        rating.save()
        return rating

    @staticmethod
    def update_rating(rating_id, score):
        """Update a rating"""
        try:
            rating = Rating.objects.get(id=rating_id)
            rating.score = score
            rating.save()
            return rating
        except Rating.DoesNotExist:
            return None

    @staticmethod
    def delete_rating(rating_id):
        """Delete a rating"""
        try:
            rating = Rating.objects.get(id=rating_id)
            rating.delete()
            return True
        except Rating.DoesNotExist:
            return False

    @staticmethod
    def get_average_rating(book_id):
        """Get average rating for a book"""
        from django.db.models import Avg
        avg = Rating.objects.filter(book_id=book_id).aggregate(Avg('score'))
        return avg['score__avg']


class WishlistDAO:
    """Data Access Object for Wishlist model"""

    @staticmethod
    def get_or_create_wishlist(customer_id):
        """Get or create wishlist for a customer"""
        wishlist, created = Wishlist.objects.get_or_create(customer_id=customer_id)
        return wishlist

    @staticmethod
    def add_to_wishlist(customer_id, book_id):
        """Add a book to wishlist"""
        try:
            wishlist = WishlistDAO.get_or_create_wishlist(customer_id)
            item, created = WishlistItem.objects.get_or_create(
                wishlist=wishlist,
                book_id=book_id
            )
            return item
        except Exception:
            return None

    @staticmethod
    def remove_from_wishlist(customer_id, book_id):
        """Remove a book from wishlist"""
        try:
            wishlist = Wishlist.objects.get(customer_id=customer_id)
            WishlistItem.objects.filter(wishlist=wishlist, book_id=book_id).delete()
            return True
        except Wishlist.DoesNotExist:
            return False

    @staticmethod
    def get_wishlist_items(customer_id):
        """Get all items in a customer's wishlist"""
        try:
            wishlist = Wishlist.objects.get(customer_id=customer_id)
            return WishlistItem.objects.filter(wishlist=wishlist)
        except Wishlist.DoesNotExist:
            return WishlistItem.objects.none()
