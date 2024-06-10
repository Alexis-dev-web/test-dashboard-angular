from dataclasses import dataclass
from utils.base_dto import BaseDto
from organization.models import DeliveredAddress


@dataclass
class DeliveredAddressDTO(BaseDto):
    country: str
    street: str
    state: str
    ext_num: str
    organization_id: str
    cologne: str = None
    pc: str = None
    is_default: bool = False
    is_active: bool = True
    int_num: str = None
    address_id: str = None
    address: DeliveredAddress = None
