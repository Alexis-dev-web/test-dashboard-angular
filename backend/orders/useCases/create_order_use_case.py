from datetime import datetime

from orders.dto import CreateOrderDTO
from orders.models import Order, OrderRepository
from .add_product_to_order_use_case import AddProductToOrderUseCase
from orders.response import OrderResponse


class CreateOrderUseCase:

    def __init__(self) -> None:
        self.order_repository = OrderRepository()
        self.add_product_use_case = AddProductToOrderUseCase()
        self.order_response = OrderResponse()

    def execute(self, request: CreateOrderDTO) -> dict:
        products_response = []
        quantity = 0 
        cost = 0.0
        delivered_days = datetime.strptime(request.delivered_date, '%Y-%m-%d') - datetime.strptime(request.order_created_date, '%Y-%m-%d')
        order = Order()
        total_orders = self.order_repository.get_total_orders()
        order.number = 1 if not total_orders else total_orders + 1
        order.provider_id = request.provider_id
        order.is_paid = request.is_paid
        order.paid_date = request.paid_date
        order.delivered_date = request.delivered_date
        order.delivered_address_id = request.delivered_address_id
        order.delivered_total_days = delivered_days.days
        order.order_created_date = request.order_created_date
        
        order.save()

        for product in request.products:
            product.order_id = order.id
            new_product = self.add_product_use_case.execute(product)
            products_response.append(new_product)
            quantity += new_product['quantity']
            cost += new_product['cost']

        order.total_price = cost
        order.total_quantity = quantity
        order.save()
    
        return self.order_response.order_with_products(order, products_response)
