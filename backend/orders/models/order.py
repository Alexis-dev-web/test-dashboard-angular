import uuid

from django.db import models
from organization.models import Organization, DeliveredAddress


class Order(models.Model):
    STATUS_CHOICE = (
        ('CREATE', 'CREATE'),
        ('CANCELLED', 'CANCELLED'),
        ('SENT', 'SENT'),
        ('DELIVERED', 'DELIVERED')
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    number = models.IntegerField()
    reason_cancelled = models.CharField(max_length=500, null=True)
    total_price = models.FloatField(default=0.0)
    total_quantity = models.FloatField(default=0.0)
    status = models.CharField(choices=STATUS_CHOICE, default='CREATE')
    delivered_on_time = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_paid = models.BooleanField(default=False)
    delivered_total_days = models.IntegerField(default=0)
    days_to_delivered = models.IntegerField(default=0)
    paid_date = models.DateField(null=True)
    real_paid_date = models.DateField(null=True)
    delivered_date = models.DateField()
    order_created_date = models.DateField()
    real_delivered_date = models.DateField(null=True)
    provider = models.ForeignKey(Organization, on_delete=models.CASCADE)
    delivered_address = models.ForeignKey(DeliveredAddress, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
