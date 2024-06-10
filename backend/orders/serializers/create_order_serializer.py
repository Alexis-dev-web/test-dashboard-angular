from rest_framework import serializers
from organization.serializers.custom_organization_validators import CustomOrganizationValidations
from organization.models import OrganizationRepository
from .add_product_to_order_serializer import AddProductToOrderSerializer


class CreateOrderSerializer(serializers.Serializer):
    total_price = serializers.FloatField(required=False)
    total_quantity = serializers.FloatField(required=False)
    is_paid = serializers.BooleanField(required=False)
    products = serializers.ListSerializer(child=AddProductToOrderSerializer(), min_length=1)
    provider_id = serializers.UUIDField()
    delivered_date = serializers.DateField()
    paid_date = serializers.DateField(required=False)
    delivered_address_id = serializers.UUIDField()
    order_created_date = serializers.DateField()

    def validate(self, data: dict):
        provider_id = data.get('provider_id')
        delivered_address_id = data.get('delivered_address_id')

        provider = OrganizationRepository().get_by_id(provider_id)
        if not provider:
            raise serializers.ValidationError('Provider does not exist')

        CustomOrganizationValidations().validate_address_organization(delivered_address_id)

        return data 
