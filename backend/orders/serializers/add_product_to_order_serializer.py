from rest_framework import serializers

from products.serializers.custom_product_validate import CustomProductValidate
from orders.serializers.custom_orders_validate import CustomOrdersValidate, Order


class AddProductToOrderSerializer(serializers.Serializer):
    quantity = serializers.FloatField()
    product_id = serializers.UUIDField()
    order_id = serializers.UUIDField(required=False, default=None)
    order = serializers.SerializerMethodField('_validet_order')

    def _validet_order(self, data: dict) -> Order:
        order = None
        order_id = data.get('order_id', None)

        if order_id:
            order = CustomOrdersValidate().validate_order_exists(order_id)

        return order

    def validate(self, data: dict) -> dict:
        product_id = data.get('product_id')

        CustomProductValidate().validate_product_exists(product_id)

        return data
