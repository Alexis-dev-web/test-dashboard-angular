from products.response import ProductResponse, Product
from products.dto import ProductDTO


class CreateOrUpdateProductUseCase:

    def __init__(self) -> None:
        self.product_response = ProductResponse()

    def execute(self, request: ProductDTO) -> ProductResponse:
        product = request.product

        if not product:
            product = Product()

        product.description = request.description
        product.name = request.name
        product.sku = request.sku
        product.image_url = request.image_url
        product.is_active = request.is_active
        product.is_sould_out = request.is_sould_out

        product.save()

        return self.product_response.to_json(product)
