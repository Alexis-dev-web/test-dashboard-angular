from products.response import ProductResponse
from products.models import ProductRepository, Product


class GetProductsUseCase:
    
    def __init__(self) -> None:
        self.product_repository = ProductRepository()
        self.product_response = ProductResponse()

    def execute(self) -> list[ProductResponse]:
        products = self.product_repository.get_all()

        return [self.product_response.to_json(product) for product in products or []]
