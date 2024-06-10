import uuid

from django.db import models

from products.models import Product
from .order import Order


class OrderProducts(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cost = models.FloatField(default=0.0)
    quantity = models.FloatField(default=0.0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)