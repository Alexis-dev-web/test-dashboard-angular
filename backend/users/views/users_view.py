import logging
from rest_framework import status as api_status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from users.useCases.get_users_use_case import GetUsersUseCase


class UsersView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def __init__(self) -> None:
        self.get_users_use_case = GetUsersUseCase()
        self.logger = logging.getLogger(__name__)

    def get(self, request):
        self.logger.info(f"UsersView#get START - Get users list ")

        try:
            users = self.get_users_use_case.execute()

            self.logger.info(f"UsersView#get SUCCESS - Get users list - users={len(users)} ")

            return Response(users, status=api_status.HTTP_200_OK)
        except Exception as error_message:
            self.logger.error(f'UsersView#get FAILURE - error to get users - message{str(error_message)})')
            return Response({"message": str(error_message)}, status=api_status.HTTP_500_INTERNAL_SERVER_ERROR)
