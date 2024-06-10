from organization.models import Organization, ProviderHasProduct


class OrganizationResponse:

    def to_json(self, organization: Organization) -> dict:
        return {
            'id': str(organization.id),
            'name': organization.name,
            'email': organization.email,
            'phone': organization.phone,
            'image_url': organization.image_url,
            'is_active': organization.is_active,
            'is_provider': organization.is_provider,
            'created_at': str(organization.created_at),
            'updated_at': str(organization.updated_at),
            'deleted_at': str(organization.deleted_at),
        }

    def product_provider_response(self, provider_product: ProviderHasProduct) -> dict:
        return {
            'id': str(provider_product.id),
            'is_active': provider_product.is_active,
            'provider_id': provider_product.provider_id,
            'product_id': provider_product.product_id,
            'created_at': str(provider_product.created_at),
            'updated_at': str(provider_product.updated_at),
            'deleted_at': str(provider_product.deleted_at),
        }
