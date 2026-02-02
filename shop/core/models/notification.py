from django.db import models


class Notification(models.Model):
    """Notification model for system notifications"""
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE, related_name='notifications')
    title = models.CharField(max_length=255)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'core'
        db_table = 'core_notification'

    def __str__(self):
        return f"Notification: {self.title}"
