import datetime
from orders.models import OrderRepository, OrderProductsRepository
from orders.response import OrderResponse
from organization.models import DeliveredAddressRepository
from products.models import ObjectivesProductRepository


class GetOrdersReportUseCase:

    def __init__(self) -> None:
        self.order_repository = OrderRepository()
        self.order_response = OrderResponse()
        self.delivered_address_repository = DeliveredAddressRepository()
        self.order_products_repository = OrderProductsRepository()
        self.objectives_product_repository = ObjectivesProductRepository()

    def execute(self):
        poduct_progress = []
        order_delivered_on_time = 0
        order_not_delivered_on_time = 0
        today = datetime.date.today()
        last_year = today.replace(year= today.year - 1)

        orders = self.order_repository.get_group_by_status(last_year)
        orders_delivered_on_time = self.order_repository.get_total_by_delivered_on_time_by_date(last_year)
        total_quantity_and_total_price = self.order_repository.get_last_year_total_quantity_by_date(last_year)
        
        next_paid = self.order_repository.get_next_paid()
        next_delivered = self.order_repository.get_next_delivere()
        delivered_address = self.delivered_address_repository.get_by_id(next_delivered.delivered_address_id)
        orders_by_year = self.order_repository.get_delivery_group_by_year()
        average_delivered = self.order_repository.get_order_average_delivered_days(last_year)

        for order in orders_delivered_on_time:
            if order['delivered_on_time']:
                order_delivered_on_time = order['total']
            else:
                order_not_delivered_on_time = order['total']

        next_delivered = self.order_response.order_with_delivered_address(next_delivered, delivered_address)

        injured_products = self.order_products_repository.get_by_product_injure(last_year)
         
        provider_delivery = self.order_repository.get_average_provider_delivered(last_year)

        objectives_product = self.objectives_product_repository.get_objectives_active(str(today.year))

        for objective in objectives_product:
            product = self.order_products_repository.get_progress_by_product(objective.product.id, last_year)
            poduct_progress.append(self.order_response.product_response.report_product_progress(product[0], objective.quantity))

        return self.order_response.report_order_response(
            next_paid=next_paid,
            next_deliver=next_delivered,
            orders_by_status=orders,
            order_delivered_on_time=order_delivered_on_time,
            order_not_delivered=order_not_delivered_on_time,
            total_quantity=total_quantity_and_total_price['total_final_quantity'],
            total_cost=total_quantity_and_total_price['total_cost'],
            orders_by_year=orders_by_year,
            average_delivered=average_delivered,
            injured_products=injured_products,
            provider_delivery=provider_delivery,
            product_progress=poduct_progress
        )
