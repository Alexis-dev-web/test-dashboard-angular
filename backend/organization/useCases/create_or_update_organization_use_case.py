from organization.models import Organization
from organization.dto import OrganizationDTO
from organization.response import OrganizationResponse


class CreateOrUpdateOrganizationUseCase:

    def __init__(self) -> None:
        self.organization_response = OrganizationResponse()

    def execute(self, request: OrganizationDTO) -> OrganizationResponse:
        organization = request.organization
        if not organization:
            organization = Organization()

        organization.name = request.name
        organization.email = request.email
        organization.image_url = request.image_url
        organization.phone = request.phone
        organization.is_active = request.is_active
        organization.is_provider = request.is_provider

        organization.save()

        return self.organization_response.to_json(organization)
