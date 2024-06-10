import uuid
import datetime

from django.db.models import Count, Sum, Q, Avg
from django.db.models.functions import TruncYear


from .order import Order


class OrderRepository:
    
    def get_by_id(self, id: uuid.UUID) -> Order:
        return Order.objects.get(pk=id)

    def get_all(self) -> list[Order]:
        return Order.objects.all()

    def get_by_status(self, status: Order.STATUS_CHOICE) -> list:
        return Order.objects.filter(status=status).all()

    def get_group_by_status(self, date) -> list:
        return Order.objects.filter(order_created_date__gte=date).values('status').annotate(total=Count('id'))

    def get_last_year_total_quantity_by_date(self, date):
        return Order.objects.filter(~Q(status='CANCELLED'))\
            .filter(order_created_date__gt=date, delivered_on_time=True).aggregate(total_cost=Sum('total_price'), total_final_quantity=Sum('total_quantity'))

    def get_total_by_delivered_on_time_by_date(self, date):
        return Order.objects.filter(status='DELIVERED').filter(delivered_date__gte=date).values('delivered_on_time').annotate(total=Count('id')).order_by('delivered_on_time')

    def get_total_orders(self) -> int:
        return Order.objects.count()

    def get_next_delivere(self):
        return Order.objects.filter(delivered_date__gt=datetime.date.today()).filter(~Q(status='CANCELLED')).order_by('delivered_date').first()

    def get_next_paid(self):
        return Order.objects.filter(paid_date__gt=datetime.date.today()).filter(~Q(status='CANCELLED')).order_by('paid_date').first()

    def get_delivery_group_by_year(self):
        return Order.objects.filter(status='DELIVERED', delivered_on_time=True).annotate(year=TruncYear('delivered_date'))\
            .values('year').annotate(total_delivered=Count('id')).order_by('year')

    def get_order_average_delivered_days(self, date):
        return Order.objects.filter(status='DELIVERED', order_created_date__gt=date)\
            .aggregate(average_days=Avg('days_to_delivered'))

    def get_average_provider_delivered(self, date):
        return Order.objects.filter(status='DELIVERED', order_created_date__gt=date)\
            .values('provider', 'provider__name')\
            .annotate(average_days=Avg('days_to_delivered'))
