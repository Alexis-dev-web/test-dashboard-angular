import uuid
from .product import Product


class ProductRepository:
    
    def get_by_id(self, id: uuid.UUID) -> Product:
        return Product.objects.get(pk=id)

    def get_by_sku(self, sku: str) -> Product:
        return Product.objects.filter(sku=sku).first()

    def get_all(self) -> list[Product]:
        return Product.objects.all()
