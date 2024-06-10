from datetime import datetime, date

from orders.dto import UpdateOrderDTO
from orders.models import Order, OrderRepository
from orders.response import OrderResponse



class UpdateOrderUseCase:

    def __init__(self) -> None:
        self.order_repository = OrderRepository()
        self.order_response = OrderResponse()

    def execute(self, request: UpdateOrderDTO) -> dict:
        order = request.order
        order.status = order.status if not request.status else request.status

        if request.status == 'CANCELLED':
            order.reason_cancelled = request.reason_cancelled

        if request.status == 'DELIVERED':
            days_to_delivered = datetime.strptime(request.real_delivered_date, '%Y-%m-%d') - datetime.combine(order.order_created_date, datetime.min.time())
            order.real_delivered_date = date.today() if not request.real_delivered_date else request.real_delivered_date
            order.delivered_on_time = datetime.strptime(order.real_delivered_date, '%Y-%m-%d') <= datetime.combine(order.delivered_date, datetime.min.time())

            order.days_to_delivered = days_to_delivered.days

        if not request.status:
            order.is_paid = request.is_paid
            order.paid_date = request.paid_date


        order.save()
        return self.order_response.to_json(order)
