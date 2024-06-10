import uuid

from django.db import models
from products.models import Product
from .organization import Organization


class ProviderHasProduct(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    price = models.FloatField(default=0.0)
    quantity = models.FloatField(default=1)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    provider = models.ForeignKey(Organization, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
