from organization.dto import AddProviderProductDTO
from organization.models import ProviderHasProduct
from organization.response import OrganizationResponse


class AddProductToProviderUseCase:

    def __init__(self) -> None:
        self.organization_response = OrganizationResponse()

    def execute(self, request: AddProviderProductDTO) -> dict:
        product = ProviderHasProduct()
        product.price = request.price
        product.product_id = request.product_id
        product.provider_id = request.provider_id

        product.save()

        return self.organization_response.product_provider_response(product)


