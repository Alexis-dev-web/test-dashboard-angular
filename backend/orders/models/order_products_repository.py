import uuid
from django.db.models import Q, Count, Sum

from .order_products import OrderProducts


class OrderProductsRepository:
    
    def get_all_by_order_id(self, order_id: uuid.UUID) -> list:
        return OrderProducts.objects.filter(order_id=order_id).all()

    def get_by_product_id(self, product_id: uuid.UUID) -> list:
        return OrderProducts.objects.filter(product_id=product_id)

    def get_by_product_injure(self, date) -> list:
        return OrderProducts.objects.filter(~Q(order__status='CANCELLED'))\
            .filter(order__order_created_date__gte=date)\
            .values('product', 'product__name').annotate(total=Count('id')).order_by('product__name')


    def get_progress_by_product(self, product_id: uuid.UUID, date) -> dict:
        return OrderProducts.objects.filter(order__order_created_date__gte=date, product_id=product_id, order__status='DELIVERED')\
            .values('product', 'product__name').annotate(total_progress=Sum('quantity')).order_by('product__name')