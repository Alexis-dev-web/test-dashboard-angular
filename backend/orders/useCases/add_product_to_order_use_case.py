from orders.dto import AddProductToOrderDTO
from organization.models import ProviderProductRepository
from orders.models import OrderProducts
from orders.response import OrderProductResponse


class AddProductToOrderUseCase:

    def __init__(self) -> None:
        self.provider_product_repository = ProviderProductRepository()
        self.order_product_response = OrderProductResponse()

    def execute(self, request: AddProductToOrderDTO) -> dict:
        order = request.order
        provider_product = self.provider_product_repository.get_by_product_id(request.product_id)

        product = OrderProducts()
        product.product_id = request.product_id
        product.order_id = request.order_id
        product.quantity = request.quantity
        product.cost = provider_product.price * request.quantity

        if order:
            order.total_price += request.cost
            order.total_quantity += request.quantity
            order.save()

        product.save()

        return self.order_product_response.to_json(product)
