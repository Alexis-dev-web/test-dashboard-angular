import logging
from rest_framework import status as api_status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.serializers import ValidationError

from organization.serializers import DeliveredAddressSerializer
from organization.dto import DeliveredAddressDTO
from organization.useCases import CreateOrUpdateUserAddressUseCase


class DeliveredAddresView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def __init__(self) -> None:
        self.logger = logging.getLogger(__name__)
        self.create_or_update_delivered_address_use_case = CreateOrUpdateUserAddressUseCase()

    def post(self, request):
        self.logger.info(f"DeliveredAddresView#post START - Create delivered addres ")

        try:
            serializers = DeliveredAddressSerializer(data=request.data)

            serializers.is_valid(raise_exception=True)

            address = self.create_or_update_delivered_address_use_case.execute(DeliveredAddressDTO.from_json(serializers.data))

            self.logger.info(f"DeliveredAddresView#post SUCCESS - Created delivered addres- addressId={address['id']} ")

            return Response(address, status=api_status.HTTP_200_OK)
        except ValidationError as error:
            self.logger.error(f'DeliveredAddresView#post FAILURE -  Created delivered addres - message{str(error.detail)})')
            return Response({"message": error.detail}, status=api_status.HTTP_400_BAD_REQUEST)
        except Exception as error_message:
            self.logger.error(f'DeliveredAddresView#post FAILURE -  Created delivered addres - message{str(error_message)})')
            return Response({"message": str(error_message.args)}, status=api_status.HTTP_500_INTERNAL_SERVER_ERROR)

    def patch(self, request):
        self.logger.info(f"DeliveredAddresView#patch START - Update delivered address ")

        try:
            new_request = {**request.data, 'update': True}

            serializers = DeliveredAddressSerializer(data=new_request)

            serializers.is_valid(raise_exception=True)

            address = self.create_or_update_delivered_address_use_case.execute(DeliveredAddressDTO.from_json(serializers.data))

            self.logger.info(f"DeliveredAddresView#patch SUCCESS - Update delivered address - addressId={address['id']} ")

            return Response(address, status=api_status.HTTP_200_OK)
        except ValidationError as error:
            self.logger.error(f'DeliveredAddresView#patch FAILURE - error to Update delivered address  - message{str(error.detail)})')
            return Response({"message": error.detail}, status=api_status.HTTP_400_BAD_REQUEST)
        except Exception as error_message:
            self.logger.error(f'DeliveredAddresView#patch FAILURE - error to Update delivered address  - message{str(error_message)})')
            return Response({"message": str(error_message.args)}, status=api_status.HTTP_500_INTERNAL_SERVER_ERROR)
