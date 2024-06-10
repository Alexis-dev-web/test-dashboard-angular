from rest_framework import serializers
from organization.models import ProviderHasProduct
from .custom_organization_validators import CustomOrganizationValidations


class ProviderProductSerializer(serializers.Serializer):
    price = serializers.FloatField()
    is_active = serializers.BooleanField(required=False)
    product_id = serializers.UUIDField(required=False)
    provider_id = serializers.UUIDField(required=False)
    update = serializers.BooleanField(required=False)
    provider_has_product = serializers.SerializerMethodField('_validate_provider_has_product')
    provider_product_id = serializers.UUIDField(required=False)

    def _validate_provider_has_product(self, data: dict) -> ProviderHasProduct:
        response = None
        update = data.get('update', False)

        if update:            
            provider_product_id = data.get('provider_product_id', None)
            validators = CustomOrganizationValidations()
            response = validators.validate_exits_provider_has_product(provider_product_id)

        return response

    def validate(self, data: dict) -> dict:
        update = data.get('update', False)
        if not update:
            product_id = data.get('product_id', None)
            provider_id = data.get('provider_id', None)
            
            validators = CustomOrganizationValidations()
            validators.validate_product_by_product_id_and_provider_id(provider_id, product_id)

        return data
