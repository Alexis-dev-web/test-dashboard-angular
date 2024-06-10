import uuid
from rest_framework import serializers
from users.models.user_repository import UserRespository, User


class CustomUserValidations:
    
    def validate_user(self, user_id: str) -> User:
        user_repository = UserRespository()

        user = user_repository.get_by_id(user_id)
        if not user:
            raise serializers.ValidationError('User does not exist')

        return user

