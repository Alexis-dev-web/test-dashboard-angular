from users.models import User


class UserResponse:

    def to_json(self, user: User):
        return {
            'id': str(user.id),
            'name': user.name,
            'email': user.email,
            'last_name': user.last_name,
            'gender': user.gender,
            'is_active': user.is_active,
            'is_superuser': user.is_superuser,
            'role': user.role,
            'created_at': str(user.created_at),
            'updated_at': str(user.updated_at),
            'deleted_at': str(user.deleted_at),
            'last_login': str(user.last_login)
        }
