import uuid

from .provider_has_products import ProviderHasProduct


class ProviderProductRepository:

    def get_by_id(self, id: uuid.UUID) -> ProviderHasProduct:
        return ProviderHasProduct.objects.get(pk=id)

    def get_by_provider_id(self, provider_id: uuid.UUID) -> list[ProviderHasProduct]:
        return ProviderHasProduct.objects.filter(provider_id=provider_id).all()

    def get_by_provider_id_and_product_id(self, provider_id: uuid.UUID, product_id: uuid.UUID) -> ProviderHasProduct:
        return ProviderHasProduct.objects.filter(product_id=product_id, provider_id=provider_id).first()

    def get_by_product_id(self, product_id: uuid.UUID) -> ProviderHasProduct:
        return ProviderHasProduct.objects.filter(product_id=product_id).first()
