from products.models import Product


class ProductResponse:

    def to_json(self, product: Product) -> dict:
        return {
            'id': product.id,
            'sku': product.sku,
            'name': product.name,
            'description': product.description,
            'image_url': product.image_url,
            'is_sould_out': product.is_sould_out,
            'is_active': product.is_active,
            'created_at': product.created_at,
        }

    def report_product_injured(self, product: dict) -> dict:
        return {
            'id': product['product'],
            'name': product['product__name'],
            'average_days': product['total']
        }

    def report_product_progress(self, product: dict, objective: int) -> dict:
        return {
            'id': product['product'],
            'name': product['product__name'],
            'total_progress': product['total_progress'],
            'objective': objective
        }
