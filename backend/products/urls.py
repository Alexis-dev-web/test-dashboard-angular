from django.urls import path

from .views import *


app_name = "products"

urlpatterns = [
    path('api/product', ProductView.as_view(), name='prduct'),
    path('api/products', ProductsView.as_view(), name='products')
]
