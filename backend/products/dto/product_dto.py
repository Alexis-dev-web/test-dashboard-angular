from dataclasses import dataclass
from utils.base_dto import BaseDto
from products.models import Product


@dataclass
class ProductDTO(BaseDto):
    sku: str
    name: str
    description: str = None
    image_url: str = None
    is_sould_out: bool = False
    is_active: bool = True
    product_id: str = None
    product: Product = None
