import uuid
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from .organization import Organization


class DeliveredAddress(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    country = models.CharField(max_length=50)
    street = models.CharField(max_length=255)
    cologne = models.CharField(max_length=255, null=True)
    state = models.CharField(max_length=100)
    ext_num = models.CharField(max_length=50)
    int_num = models.CharField(max_length=100, null=True)
    pc = models.CharField(max_length=50, null=True)
    is_active = models.BooleanField(default=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
    object_id = GenericForeignKey('content_type', 'organization_id')
