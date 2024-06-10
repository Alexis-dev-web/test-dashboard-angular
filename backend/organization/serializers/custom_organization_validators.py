import uuid
from rest_framework import serializers

from utils.error_messages import messages
from organization.models import *


class CustomOrganizationValidations:

    def __init__(self) -> None:
        self.delivered_address_repository = DeliveredAddressRepository()
        self.organization_repository = OrganizationRepository()
        self.provider_product_repository = ProviderProductRepository()

    def validate_address_organization(self, address_id: uuid.UUID) -> DeliveredAddress:
        if not address_id:
            raise serializers.ValidationError(messages['address_id_required'])

        try:
            return self.delivered_address_repository.get_by_id(address_id)
        except:
            raise serializers.ValidationError(messages['address_not_exist'])

    def validate_organization(self, organization_id: uuid.UUID) -> Organization:
        if not organization_id:
            raise serializers.ValidationError(messages['organization_id_required'])

        try:
            return self.organization_repository.get_by_id(organization_id)
        except:
            raise serializers.ValidationError(messages['organization_not_exist'])

    def validate_exits_provider_has_product(self, provider_product_id: uuid.UUID) -> ProviderHasProduct:
        if not provider_product_id:
            raise serializers.ValidationError(messages['provider_product_id_required'])

        try:
            return self.provider_product_repository.get_by_id(provider_product_id)
        except:
            raise serializers.ValidationError(messages['provider_product_not_exist'])

    def validate_product_by_product_id_and_provider_id(self, provider_id: uuid.UUID, product_id: uuid.UUID) -> ProviderHasProduct:
        if not provider_id:
            raise serializers.ValidationError(messages['provider_id_required'])

        if not product_id:
            raise serializers.ValidationError(messages['product_id_required'])

        try:
            return self.provider_product_repository.get_by_provider_id_and_product_id(provider_id, product_id)
        except:
            raise serializers.ValidationError(messages['provider_product_not_exist'])
