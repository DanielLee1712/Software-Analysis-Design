from django.db import models


class PromotionEvent(models.Model):
    """Promotion Event model for marketing campaigns"""
    id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    banner_url = models.CharField(max_length=255, blank=True, null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    target_category = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        app_label = 'core'
        db_table = 'core_promotion_event'

    def __str__(self):
        return self.event_name
