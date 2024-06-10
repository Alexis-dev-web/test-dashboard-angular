import uuid

from .delivered_address import DeliveredAddress


class DeliveredAddressRepository:

    def get_by_id(self, id: uuid.UUID) -> DeliveredAddress:
        return DeliveredAddress.objects.get(pk=id)
