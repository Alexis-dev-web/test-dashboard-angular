from dataclasses import dataclass
from utils.base_dto import BaseDto
from orders.models import Order


@dataclass
class AddProductToOrderDTO(BaseDto):
    quantity: float
    product_id: str
    order_id: str = None
    order: Order = None
