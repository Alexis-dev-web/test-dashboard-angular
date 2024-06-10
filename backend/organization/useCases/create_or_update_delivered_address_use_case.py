from organization.models import DeliveredAddress
from organization.response import DeliveredAddressResponse
from organization.dto import DeliveredAddressDTO


class CreateOrUpdateUserAddressUseCase:

    def __init__(self) -> None:
        self.addres_response = DeliveredAddressResponse()

    def execute(self, request: DeliveredAddressDTO) -> DeliveredAddressResponse:
        address = request.address

        if not address:
            address = DeliveredAddress()
            address.organization_id = request.organization_id

        address.country = request.country
        address.street = request.street
        address.pc = request.pc
        address.cologne = request.cologne
        address.ext_num = request.ext_num
        address.int_num = request.int_num
        address.is_default = request.is_default
        address.is_active = request.is_active

        address.save()

        return self.addres_response.to_json(address)
