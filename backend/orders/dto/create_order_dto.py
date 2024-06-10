from dataclasses import dataclass
from datetime import date
from utils.base_dto import BaseDto
from .add_product_order_dto import AddProductToOrderDTO


@dataclass
class CreateOrderDTO(BaseDto):
    delivered_address_id: str
    delivered_date: date
    paid_date: date
    order_created_date: date
    provider_id: str
    products: list[AddProductToOrderDTO]
    total_price: float = 0.0
    total_quantity: float = 0
    is_paid: bool = False

    def __post_init__(self):
        self.products = [AddProductToOrderDTO.from_json(product) for product in self.products or []]
