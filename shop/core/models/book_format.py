from django.db import models


class BookImage(models.Model):
    """Book cover/images model"""
    id = models.AutoField(primary_key=True)
    book = models.OneToOneField('Book', on_delete=models.CASCADE, related_name='image')
    image_url = models.CharField(max_length=255)
    image_type = models.CharField(max_length=50)

    class Meta:
        app_label = 'core'
        db_table = 'core_book_image'

    def __str__(self):
        return f"Image for {self.book.title}"


class EBook(models.Model):
    """E-Book model for digital books"""
    id = models.AutoField(primary_key=True)
    book = models.OneToOneField('Book', on_delete=models.CASCADE, related_name='ebook')
    file_size = models.DecimalField(max_digits=10, decimal_places=2)
    format = models.CharField(max_length=50)
    download_link = models.CharField(max_length=255)

    class Meta:
        app_label = 'core'
        db_table = 'core_ebook'

    def __str__(self):
        return f"E-Book: {self.book.title}"


class AudioBook(models.Model):
    """AudioBook model for audio books"""
    id = models.AutoField(primary_key=True)
    book = models.OneToOneField('Book', on_delete=models.CASCADE, related_name='audiobook')
    file_size = models.DecimalField(max_digits=10, decimal_places=2)
    format = models.CharField(max_length=50)
    download_link = models.CharField(max_length=255)

    class Meta:
        app_label = 'core'
        db_table = 'core_audio_book'

    def __str__(self):
        return f"AudioBook: {self.book.title}"
