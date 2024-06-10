from rest_framework import serializers
from utils.error_messages import messages

from .custom_organization_validators import CustomOrganizationValidations
from organization.models import DeliveredAddress


class DeliveredAddressSerializer(serializers.Serializer):
    street = serializers.CharField(max_length=50, error_messages={'blank': messages['street_required'], 'required': messages['street_required']})
    cologne = serializers.CharField(max_length=255, required=False)
    country = serializers.CharField(max_length=50)
    state = serializers.CharField(max_length=100)
    ext_num = serializers.CharField(max_length=50)
    int_num = serializers.CharField(max_length=100, required=False)
    pc = serializers.CharField(max_length=50, required=False)
    is_active = serializers.BooleanField(required=False)
    organization_id = serializers.UUIDField()
    address_id = serializers.UUIDField(required=False)
    update = serializers.BooleanField(required=False)
    address = serializers.SerializerMethodField('_validate_address_exist')

    def _validate_address_exist(self, data: dict) -> DeliveredAddress:
        address = None
        update = data.get('update', False)

        if update:            
            address_id = data.get('address_id', None)
            validators = CustomOrganizationValidations()
            address = validators.validate_address_organization(address_id)

        return address

    def validate(self, data: dict) -> dict:
        validators = CustomOrganizationValidations()
        organization_id = data.get('organization_id')

        validators.validate_organization(organization_id)

        return data
