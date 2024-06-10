from orders.models import OrderProducts


class OrderProductResponse:

    def to_json(self, order_product: OrderProducts) -> dict:
        return {
            'id': str(order_product.id),
            'cost': order_product.cost,
            'quantity': order_product.quantity,
            'product_id': order_product.product_id,
            'order_id': order_product.order.id
        }
