import uuid

from .organization import Organization


class OrganizationRepository:
    
    def get_by_id(self, id: uuid.UUID) -> Organization:
        return Organization.objects.get(pk=id)

    def get_all(self) -> list:
        return Organization.objects.all()

    def get_by_status(self, status: bool = True) -> list:
        return Organization.objects.filter(status=status).all()
