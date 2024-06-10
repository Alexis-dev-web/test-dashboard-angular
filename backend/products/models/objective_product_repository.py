import uuid
from .objectives_product import ObjectivesProduct


class ObjectivesProductRepository:
    
    def get_by_id(self, id: uuid.UUID) -> ObjectivesProduct:
        return ObjectivesProduct.objects.get(pk=id)
    
    def get_by_year(self, year: str) -> ObjectivesProduct:
        return ObjectivesProduct.objects.filter(year=year, is_active=True)

    def get_objectives_active(self, year) -> list:
        return ObjectivesProduct.objects.filter(is_active=True, year=year).all()
