from rest_framework import serializers
from .custom_organization_validators import CustomOrganizationValidations, Organization


class OrganizationSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    email = serializers.EmailField(max_length=255)
    image_url = serializers.EmailField(max_length=255, required=False)
    is_active = serializers.BooleanField(required=False)
    is_provider = serializers.BooleanField(required=False)
    phone = serializers.CharField(max_length=11, required=False)
    update = serializers.BooleanField(required=False)
    organization_id = serializers.UUIDField(required=False)
    organization = serializers.SerializerMethodField('_validate_organization')

    def _validate_organization(self, data: dict) -> Organization:
        organization = None
        update = data.get('update', False)

        if update:
            validators = CustomOrganizationValidations()
            organization = validators.validate_organization(data.get('organization_id', False))

        return organization
