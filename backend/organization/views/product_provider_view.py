import logging
from rest_framework import status as api_status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.serializers import ValidationError

from organization.serializers import ProviderProductSerializer
from organization.dto import AddProviderProductDTO
from organization.useCases import AddProductToProviderUseCase


class ProductProviderView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def __init__(self) -> None:
        self.logger = logging.getLogger(__name__)
        self.add_product_to_provider_use_case = AddProductToProviderUseCase()

    def post(self, request):
        self.logger.info(f"ProductProviderView#post START - Add product to provider")

        try:
            serializers = ProviderProductSerializer(data=request.data)

            serializers.is_valid(raise_exception=True)

            product = self.add_product_to_provider_use_case.execute(AddProviderProductDTO.from_json(serializers.data))

            self.logger.info(f"ProductProviderView#post SUCCESS - Add product to provider- productId={product['id']} ")

            return Response(product, status=api_status.HTTP_200_OK)
        except ValidationError as error:
            self.logger.error(f'ProductProviderView#post FAILURE -  Add product to provider - message{str(error.detail)})')
            return Response({"message": error.detail}, status=api_status.HTTP_400_BAD_REQUEST)
        except Exception as error_message:
            self.logger.error(f'ProductProviderView#post FAILURE -  Add product to provider - message{str(error_message)})')
            return Response({"message": str(error_message.args)}, status=api_status.HTTP_500_INTERNAL_SERVER_ERROR)
