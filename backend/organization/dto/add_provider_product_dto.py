from dataclasses import dataclass
from utils.base_dto import BaseDto
from organization.models import ProviderHasProduct


@dataclass
class AddProviderProductDTO(BaseDto):
    price: float
    provider_has_product: ProviderHasProduct = None
    product_id: str = None
    provider_id: str = None
    is_active: bool = True
