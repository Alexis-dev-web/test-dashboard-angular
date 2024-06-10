from organization.models import DeliveredAddress


class DeliveredAddressResponse:

    def to_json(self, delivered_address: DeliveredAddress) -> dict:
        return {
            'id': str(delivered_address.id),
            'country': delivered_address.country,
            'street': delivered_address.street,
            'cologne': delivered_address.cologne,
            'state': delivered_address.state,
            'ext_num': delivered_address.ext_num,
            'int_num': delivered_address.int_num,
            'pc': delivered_address.pc,
            'organization_id': delivered_address.organization.id,
            'is_active': delivered_address.is_active,
            'created_at': str(delivered_address.created_at),
            'updated_at': str(delivered_address.updated_at),
        }
