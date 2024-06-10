import logging
from rest_framework import status as api_status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.serializers import ValidationError

from products.useCases import CreateOrUpdateProductUseCase
from products.dto import ProductDTO
from products.serializers.create_or_update_product_serializer import CreateOrUpdateProductSerializer


class ProductView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def __init__(self) -> None:
        self.logger = logging.getLogger(__name__)
        self.create_or_update_product_use_case = CreateOrUpdateProductUseCase()

    def post(self, request):
        self.logger.info(f"ProductView#post START - Create product - userAgent={request.META['HTTP_USER_AGENT']}")

        try:
            serializer = CreateOrUpdateProductSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            product = self.create_or_update_product_use_case.execute(ProductDTO.from_json(serializer.data))

            self.logger.info(f"ProductView#post SUCCESS - Created product- productId={product['id']} ")

            return Response(product, status=api_status.HTTP_201_CREATED)
        except ValidationError as error:
            self.logger.error(f'UsersView#patch FAILURE - error to get users - message{str(error.detail)})')
            return Response({"message": error.detail}, status=api_status.HTTP_400_BAD_REQUEST)
        except Exception as error_message:
            self.logger.error(f'ProductView#post FAILURE - error to get users - message{str(error_message)})')
            return Response({"message": str(error_message)}, status=api_status.HTTP_500_INTERNAL_SERVER_ERROR)

    def patch(self, request):
        self.logger.info(f"ProductView#patch START - Update product - userAgent={request.META['HTTP_USER_AGENT']}")

        try:
            new_request = {**request.data, 'update': True}
            serializer = CreateOrUpdateProductSerializer(data=new_request)
            serializer.is_valid(raise_exception=True)
            
            product = self.create_or_update_product_use_case.execute(ProductDTO.from_json(serializer.data))

            self.logger.info(f"ProductView#patch SUCCESS - Updated product- productId={product['id']} ")

            return Response(product, status=api_status.HTTP_201_CREATED)
        except ValidationError as error:
            self.logger.error(f'ProductView#patch FAILURE - Updated produc- message{str(error.detail)})')
            return Response({"message": error.detail}, status=api_status.HTTP_400_BAD_REQUEST)
        except Exception as error_message:
            self.logger.error(f'ProductView#patch FAILURE - Updated produc - message{str(error_message)})')
            return Response({"message": str(error_message)}, status=api_status.HTTP_500_INTERNAL_SERVER_ERROR)
