from django.db import models


class User(models.Model):
    """Base User model for authentication"""
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'core'
        db_table = 'core_user'

    def __str__(self):
        return self.username


class Admin(models.Model):
    """Admin user model"""
    id = models.AutoField(primary_key=True)

    class Meta:
        app_label = 'core'
        db_table = 'core_admin'

    def __str__(self):
        return "Admin"


class Staff(models.Model):
    """Staff user model"""
    id = models.AutoField(primary_key=True)
    dstaff = models.CharField(max_length=255)
    role = models.CharField(max_length=255)

    class Meta:
        app_label = 'core'
        db_table = 'core_staff'

    def __str__(self):
        return f"Staff: {self.role}"
