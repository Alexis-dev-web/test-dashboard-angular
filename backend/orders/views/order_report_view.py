import logging
from rest_framework import status as api_status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
# from rest_framework_simplejwt.authentication import JWTAuthentication

from orders.useCases import GetOrdersReportUseCase


class OrderReportView(APIView):
    permission_classes = [AllowAny]

    def __init__(self, ) -> None:
        self.logger = logging.getLogger(__name__)
        self.get_orders_report_use_case = GetOrdersReportUseCase()

    def get(self, request):
        self.logger.info(f"OrderReportView#get START - Create order - userAgent={request.META['HTTP_USER_AGENT']}")

        try:
            report = self.get_orders_report_use_case.execute()

            self.logger.info(f"OrderReportView#get SUCCESS - Get report")

            return Response(report, status=api_status.HTTP_200_OK)
        except Exception as error_message:
            self.logger.error(f'OrderReportView#get FAILURE - error to get report - message{str(error_message)})')
            return Response({"message": str(error_message)}, status=api_status.HTTP_500_INTERNAL_SERVER_ERROR)
