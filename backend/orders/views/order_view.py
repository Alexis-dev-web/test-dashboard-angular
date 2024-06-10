import logging
from rest_framework import status as api_status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import serializers

from orders.useCases import CreateOrderUseCase, UpdateOrderUseCase
from orders.serializers import CreateOrderSerializer, UpdateOrderSerializer
from orders.dto import CreateOrderDTO, UpdateOrderDTO


class OrderView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def __init__(self) -> None:
        self.logger = logging.getLogger(__name__)
        self.create_order_use_case = CreateOrderUseCase()
        self.update_order_case = UpdateOrderUseCase()

    def post(self, request):
        self.logger.info(f"OrderView#post START - Create order - userAgent={request.META['HTTP_USER_AGENT']}")

        try:
            serializer = CreateOrderSerializer(data=request.data)

            serializer.is_valid(raise_exception=True)

            order = self.create_order_use_case.execute(CreateOrderDTO.from_json(serializer.data))

            self.logger.info(f"OrderView#post SUCCESS - Created product- orderId={order['id']} ")

            return Response(order, status=api_status.HTTP_201_CREATED)
        except serializers.ValidationError as error:
            self.logger.error(f'OrderView#post FAILURE - error to create order - message{str(error.detail)})')
            return Response({"message": error.detail}, status=api_status.HTTP_400_BAD_REQUEST)
        except Exception as error_message:
            self.logger.error(f'OrderView#post FAILURE - error to create order - message{str(error_message)})')
            return Response({"message": str(error_message)}, status=api_status.HTTP_500_INTERNAL_SERVER_ERROR)

    def patch(self, request):
        self.logger.info(f"OrderView#patch START - Update order - userAgent={request.META['HTTP_USER_AGENT']}")

        try:
            serializer = UpdateOrderSerializer(data=request.data)

            serializer.is_valid(raise_exception=True)

            order = self.update_order_case.execute(UpdateOrderDTO.from_json(serializer.data))

            self.logger.info(f"OrderView#patch SUCCESS - Udated product- orderId={order['id']} ")

            return Response(order, status=api_status.HTTP_200_OK)
        except serializers.ValidationError as error:
            self.logger.error(f'OrderView#patch FAILURE - error to update order - message{str(error.detail)})')
            return Response({"message": error.detail}, status=api_status.HTTP_400_BAD_REQUEST)
        except Exception as error_message:
            self.logger.error(f'OrderView#patch FAILURE - error to update order - message{str(error_message)})')
            return Response({"message": str(error_message)}, status=api_status.HTTP_500_INTERNAL_SERVER_ERROR)
