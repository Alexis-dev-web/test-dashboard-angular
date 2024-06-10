import logging
from rest_framework import status as api_status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.serializers import ValidationError

from organization.serializers import OrganizationSerializer
from organization.useCases import CreateOrUpdateOrganizationUseCase
from organization.dto import OrganizationDTO


class OrganizationView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def __init__(self) -> None:
        self.logger = logging.getLogger(__name__)
        self.create_or_update_organization_use_case = CreateOrUpdateOrganizationUseCase()

    def post(self, request):
        self.logger.info(f"OrganizationView#post START - Create organization ")

        try:
            serializers = OrganizationSerializer(data=request.data)

            serializers.is_valid(raise_exception=True)

            organization = self.create_or_update_organization_use_case.execute(OrganizationDTO.from_json(serializers.data))

            self.logger.info(f"OrganizationView#post SUCCESS - Created organization- organizationId={organization['id']} ")

            return Response(organization, status=api_status.HTTP_200_OK)
        except ValidationError as error:
            self.logger.error(f'OrganizationView#post FAILURE - error to create organization - message{str(error.detail)})')
            return Response({"message": error.detail}, status=api_status.HTTP_400_BAD_REQUEST)
        except Exception as error_message:
            self.logger.error(f'OrganizationView#post FAILURE - error to create organization - message{str(error_message)})')
            return Response({"message": str(error_message.args)}, status=api_status.HTTP_500_INTERNAL_SERVER_ERROR)

    def patch(self, request):
        self.logger.info(f"OrganizationView#patch START - Update organization ")

        try:
            new_request = {**request.data, 'update': True}

            serializers = OrganizationSerializer(data=new_request)

            serializers.is_valid(raise_exception=True)

            organization = self.create_or_update_organization_use_case.execute(OrganizationDTO.from_json(serializers.data))

            self.logger.info(f"OrganizationView#patch SUCCESS - Update organization- organizationId={organization['id']} ")

            return Response(organization, status=api_status.HTTP_200_OK)
        except ValidationError as error:
            self.logger.error(f'OrganizationView#patch FAILURE - error update organization - message{str(error.detail)})')
            return Response({"message": error.detail}, status=api_status.HTTP_400_BAD_REQUEST)
        except Exception as error_message:
            self.logger.error(f'OrganizationView#patch FAILURE - error update organization - message{str(error_message)})')
            return Response({"message": str(error_message.args)}, status=api_status.HTTP_500_INTERNAL_SERVER_ERROR)
