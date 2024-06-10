from django.urls import path

from .views import *


app_name = "organization"

urlpatterns = [
    path('api/organization', OrganizationView.as_view(), name='organization'),
    path('api/organization/address', DeliveredAddresView.as_view(), name='deliveredAddress'),
    path('api/organization/product', ProductProviderView.as_view(), name='productProvider'),
]
