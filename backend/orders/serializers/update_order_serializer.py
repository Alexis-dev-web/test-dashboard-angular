from rest_framework import serializers
from organization.models import OrganizationRepository
from orders.models import Order
from .add_product_to_order_serializer import AddProductToOrderSerializer
from .custom_orders_validate import CustomOrdersValidate


class UpdateOrderSerializer(serializers.Serializer):
    order_id = serializers.UUIDField()
    reason_cancelled = serializers.CharField(required=False, max_length=500)
    total_price = serializers.FloatField(required=False)
    total_quantity = serializers.FloatField(required=False)
    is_paid = serializers.BooleanField(required=False)
    status = serializers.ChoiceField(Order.STATUS_CHOICE, required=False)
    is_active = serializers.BooleanField(required=False)
    provider_id = serializers.UUIDField(required=False)
    real_paid_date = serializers.DateField(required=False)
    real_delivered_date = serializers.DateField(required=False)
    paid_date = serializers.DateField(required=False)
    delivered_date = serializers.DateField(required=False)

    order = serializers.SerializerMethodField('_validate_order')
    delivered_address_id = serializers.UUIDField(required=False)

    def _validate_order(self, data: dict) -> Order:
        order_id = data.get('order_id', None)
        order = CustomOrdersValidate().validate_order_exists(order_id)
  
        return order

    def validate(self, data: dict) -> dict:
        provider_id = data.get('provider_id')
        status = data.get('status', None)

        if not status:
            provider = OrganizationRepository().get_by_id(provider_id)

            if not provider:
                raise serializers.ValidationError('Provider does not exist')

        return data
