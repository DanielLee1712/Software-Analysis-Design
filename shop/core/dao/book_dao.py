from core.models.book import Book
from core.models.author import Author


class BookDAO:
    """Data Access Object for Book model - handles all book-related database operations"""

    @staticmethod
    def get_all_books():
        """
        Retrieve all books from the database
        
        Returns:
            QuerySet: All Book objects
        """
        return Book.objects.all()

    @staticmethod
    def get_book_by_id(book_id):
        """
        Retrieve a single book by ID
        
        Args:
            book_id (int): The ID of the book to retrieve
            
        Returns:
            Book: The Book object or None if not found
        """
        try:
            return Book.objects.get(id=book_id)
        except Book.DoesNotExist:
            return None

    @staticmethod
    def get_books_by_category(category_id):
        """
        Retrieve books by category
        
        Args:
            category_id (int): The ID of the category
            
        Returns:
            QuerySet: Books in the specified category
        """
        return Book.objects.filter(category_id=category_id)

    @staticmethod
    def get_books_by_author(author_id):
        """
        Retrieve books by author
        
        Args:
            author_id (int): The ID of the author
            
        Returns:
            QuerySet: Books by the specified author
        """
        return Book.objects.filter(author_id=author_id)

    @staticmethod
    def create_book(title, author_id=None, publisher_id=None, category_id=None, 
                   price=0, stock=0, description="", isbn=""):
        """
        Create a new book in the database
        
        Args:
            title (str): Book title
            author_id (int): Book author ID (optional)
            publisher_id (int): Publisher ID (optional)
            category_id (int): Category ID (optional)
            price (float): Book price
            stock (int): Stock quantity
            description (str): Book description
            isbn (str): ISBN number
            
        Returns:
            Book: The newly created Book object
        """
        book = Book(
            title=title,
            author_id=author_id,
            publisher_id=publisher_id,
            category_id=category_id,
            price=price,
            stock=stock,
            description=description,
            isbn=isbn
        )
        book.save()
        return book

    @staticmethod
    def update_book(book_id, **kwargs):
        """
        Update a book's details
        
        Args:
            book_id (int): The ID of the book to update
            **kwargs: Fields to update
            
        Returns:
            Book: The updated Book object or None if not found
        """
        try:
            book = Book.objects.get(id=book_id)
            for key, value in kwargs.items():
                if hasattr(book, key):
                    setattr(book, key, value)
            book.save()
            return book
        except Book.DoesNotExist:
            return None

    @staticmethod
    def delete_book(book_id):
        """
        Delete a book
        
        Args:
            book_id (int): The ID of the book to delete
            
        Returns:
            bool: True if deleted, False if not found
        """
        try:
            book = Book.objects.get(id=book_id)
            book.delete()
            return True
        except Book.DoesNotExist:
            return False

    @staticmethod
    def search_books(query):
        """
        Search books by title or description
        
        Args:
            query (str): Search query
            
        Returns:
            QuerySet: Books matching the query
        """
        from django.db.models import Q
        return Book.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )

    @staticmethod
    def update_stock(book_id, quantity):
        """
        Update the stock of a book
        
        Args:
            book_id (int): The ID of the book
            quantity (int): The new quantity
        """
        book = BookDAO.get_book_by_id(book_id)
        if book:
            book.stock = quantity
            book.save()
