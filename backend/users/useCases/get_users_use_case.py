from users.models import UserRespository
from users.response import UserResponse


class GetUsersUseCase:

    def __init__(self) -> None:
        self.user_repository = UserRespository()
        self.user_response = UserResponse()

    def execute(self) -> list[UserResponse]:
        users = self.user_repository.get_all()

        return [self.user_response.to_json(user) for user in users or []]
