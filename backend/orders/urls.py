from django.urls import path

from .views import *


app_name = "orders"

urlpatterns = [
    path('api/order', OrderView.as_view(), name='order'),
    path('api/orders/report', OrderReportView.as_view(), name='orderReport')
]
