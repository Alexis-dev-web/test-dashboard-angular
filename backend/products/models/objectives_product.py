import uuid

from django.db import models
from .product import Product


class ObjectivesProduct(models.Model):
    TIME = (
          ('YEARLY', 'YEARLY'),
          ('MONTHLY', 'MONTHLY'),
          ('WEEKLY', 'WEEKLY')
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    time = models.CharField(max_length=50, choices=TIME, default='YEARLY')
    year = models.CharField(max_length=100)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
