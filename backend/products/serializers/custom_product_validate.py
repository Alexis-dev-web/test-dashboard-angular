import uuid

from rest_framework import serializers
from utils.error_messages import messages
from products.models import Product, ProductRepository


class CustomProductValidate:
    
    def __init__(self) -> None:
        self.product_repository = ProductRepository()

    def validate_product_exists(self, product_id: uuid.UUID) -> Product:

        if not product_id:
            raise serializers.ValidationError(messages['product_id_required'])
        
        try:
            return self.product_repository.get_by_id(product_id)
        except:
            raise serializers.ValidationError(messages['product_not_exist'])
