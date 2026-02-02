from core.models.author import Author


class AuthorDAO:
    """Data Access Object for Author model"""

    @staticmethod
    def get_all_authors():
        """Get all authors"""
        return Author.objects.all()

    @staticmethod
    def get_author_by_id(author_id):
        """Get author by ID"""
        try:
            return Author.objects.get(id=author_id)
        except Author.DoesNotExist:
            return None

    @staticmethod
    def create_author(name, bio="", email=""):
        """Create a new author"""
        author = Author(name=name, bio=bio, email=email)
        author.save()
        return author

    @staticmethod
    def update_author(author_id, **kwargs):
        """Update author details"""
        try:
            author = Author.objects.get(id=author_id)
            for key, value in kwargs.items():
                if hasattr(author, key):
                    setattr(author, key, value)
            author.save()
            return author
        except Author.DoesNotExist:
            return None

    @staticmethod
    def delete_author(author_id):
        """Delete an author"""
        try:
            author = Author.objects.get(id=author_id)
            author.delete()
            return True
        except Author.DoesNotExist:
            return False

    @staticmethod
    def search_authors(query):
        """Search authors by name"""
        from django.db.models import Q
        return Author.objects.filter(Q(name__icontains=query))
