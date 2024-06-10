import uuid

from users.serializers.custom_user_validations import CustomUserValidations, User
from users.response import UserResponse


class GetUserUseCase:
    
    def __init__(self) -> None:
        self.user_response = UserResponse()
        self.custom_validators = CustomUserValidations()

    def execute(self, user_id: uuid.UUID) -> UserResponse:
        user = self.custom_validators.validate_user(user_id)

        return self.user_response.to_json(user)

