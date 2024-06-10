from dataclasses import dataclass
from utils.base_dto import BaseDto
from organization.models import Organization


@dataclass
class OrganizationDTO(BaseDto):
    name: str
    email: str
    image_url: str = None
    is_active: bool = True
    is_provider: bool = False
    phone: str = None
    organization: Organization = None

