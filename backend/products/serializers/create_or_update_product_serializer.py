from rest_framework import serializers
from products.models import Product, ProductRepository
from .custom_product_validate import CustomProductValidate

class CreateOrUpdateProductSerializer(serializers.Serializer):
    sku = serializers.CharField(max_length=255)
    name = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=500, required=False)
    image_url = serializers.CharField(max_length=255, required=False)
    is_sould_out = serializers.BooleanField(required=False)
    is_active = serializers.BooleanField(required=False)
    product_id = serializers.UUIDField(required=False)
    product = serializers.SerializerMethodField('_validate_get_product')
    update = serializers.BooleanField(required=False)

    def _validate_get_product(self, data: dict) -> Product:
        product = None
        update = data.get('update', False)

        if update:
            product_id = data.get('product_id', None)

            product = CustomProductValidate().validate_product_exists(product_id)

        return product

    def validate(self, data: dict) -> dict:
        update = data.get('update', False)
        product_id = data.get('product_id', None)
        sku = data.get('sku', None)

        product = ProductRepository().get_by_sku(sku)
        if (update and product and product.id != product_id) or (not update and product):
            raise serializers.ValidationError('Sku already exist')

        return data
