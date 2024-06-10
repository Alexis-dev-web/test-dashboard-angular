from orders.models import Order
from organization.response import DeliveredAddressResponse
from organization.models import DeliveredAddress
from products.response import ProductResponse


class OrderResponse:

    def __init__(self) -> None:
        self.product_response = ProductResponse()

    def to_json(self, order: Order) -> dict:
        return {
            'id': str(order.id),
            'total_price': order.total_price,
            'quantity': order.total_quantity,
            'provider_id': order.provider_id,
            'status': order.status,
            'is_paid': order.is_paid,
            'is_active': order.is_active,
            'paid_date': (order.paid_date),
            'real_paid_date': str(order.real_paid_date),
            'number': order.number,
            'delivered_total_days': order.delivered_total_days,
            'delivered_address_id': order.delivered_address_id,
            'real_delivered_date': order.real_delivered_date,
            'reason_cancelled': order.reason_cancelled,
            'delivered_on_time': order.delivered_on_time,
            'delivered_date': order.delivered_date,
            'created_at': str(order.created_at),
            'updated_at': str(order.updated_at),
            'order_created_date': str(order.order_created_date)
        }

    def order_with_products(self, order: Order, products: list) -> dict:
        order = self.to_json(order)
        order['products'] = products

        return order

    def report_order_response(self, next_paid: Order, next_deliver: dict, orders_by_status: list,
                            average_delivered: dict, provider_delivery: list[dict], product_progress: list[dict],
                            order_delivered_on_time: int, order_not_delivered: int, injured_products: list[dict],
                            total_quantity: float, total_cost: float, orders_by_year: list = []):

        return {
            'next_order_paid': self.to_json(next_paid),
            'next_order_delivered': next_deliver,
            'status': self.order_by_status(orders_by_status),
            'orders_delivered_on_time': order_delivered_on_time,
            'order_not_delivered': order_not_delivered,
            'total_quantity': total_quantity,
            'total_cost': total_cost,
            'orders_by_year': [self.order_by_year(order) for order in orders_by_year or []],
            'average_delivered': average_delivered['average_days'],
            'provider_delivery': [self.report_providerd(item) for item in provider_delivery or []],
            'injured_products': [self.product_response.report_product_injured(item) for item in injured_products or []],
            'product_progress': product_progress
        }

    def order_by_status(self, orders: list) -> dict:
        response = {
            'active': 0,
            'cancelled': 0,
            'delivered': 0
        }

        for order in orders:
            if order['status'] == 'DELIVERED':
                response['delivered'] = order['total']
            elif order['status'] == 'CANCELLED':
                response['cancelled'] = order['total']
            else:
                response['active'] += order['total']

        return response

    def order_by_year(self, year: dict) -> dict:
        return {
            'year': str(year['year'].year),
            'total_delivered': year['total_delivered']
        }

    def order_with_delivered_address(self, order: Order, address: DeliveredAddress) -> dict:
        order = self.to_json(order)
        order['address'] = DeliveredAddressResponse().to_json(address)

        return order
    
    def report_providerd(self, provider: dict) -> dict:
        return {
            'id': provider['provider'],
            'name': provider['provider__name'],
            'average_days': provider['average_days'],
        }


    