import logging
from rest_framework import status as api_status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from products.useCases import GetProductsUseCase


class ProductsView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def __init__(self) -> None:
        self.logger = logging.getLogger(__name__)
        self.get_products_use_case = GetProductsUseCase()

    def get(self, request):
        self.logger.info(f"ProductsView#get START - Get products list ")

        try:
            products = self.get_products_use_case.execute()

            self.logger.info(f"ProductsView#get SUCCESS - Get products list - users={len(products)} ")

            return Response(products, status=api_status.HTTP_200_OK)
        except Exception as error_message:
            self.logger.error(f'ProductsView#get FAILURE - error to get products - message{str(error_message)})')
            return Response({"message": str(error_message)}, status=api_status.HTTP_500_INTERNAL_SERVER_ERROR)
