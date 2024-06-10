import uuid

from rest_framework.serializers import ValidationError
from utils.error_messages import messages
from orders.models import OrderRepository, Order


class CustomOrdersValidate:
    
    def __init__(self) -> None:
        self.order_repository = OrderRepository()

    def validate_order_exists(self, order_id: uuid.UUID) -> Order:
        if not order_id:
            raise ValidationError(messages['order_id_required'])

        try:
            return self.order_repository.get_by_id(order_id)
        except:
            raise ValidationError(messages['order_not_exist'])
