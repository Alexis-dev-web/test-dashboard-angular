from dataclasses import dataclass
from datetime import date
from utils.base_dto import BaseDto
from orders.models import Order


@dataclass
class UpdateOrderDTO(BaseDto):
    order_id: str
    order: Order
    delivered_address_id: date = None
    delivered_date: date = None
    is_active: bool = False
    is_paid: bool = False
    paid_date: date = None
    provider_id: str = None
    real_delivered_date: str = None
    real_paid_date: date =  None
    reason_cancelled: str = None
    status: str = None
    total_price: float = 0.0
    total_quantity: float = 0

