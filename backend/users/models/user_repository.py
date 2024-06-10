from users.models import User


class UserRespository:

    def get_all(self) -> list:
        return User.objects.all()

    def get_by_id(self, id) -> User:
        return User.objects.get(pk=id)
