import uuid

from django.contrib.auth.models import (  # noqa: E501
    AbstractBaseUser,
    PermissionsMixin,
    UserManager
)

from django.db import models


class CustomUserManager(UserManager):
    def _create_user(self, name, email, password, **extra_fields):
        if not email:
            raise ValueError("You have not provided a valid e-mail address")

        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, name=None, email=None, password=None, **extra_fields):  # noqa: E501
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(name, email, password, **extra_fields)

    def create_superuser(self, name=None, email=None, password=None, **extra_fields):  # noqa: E501
        extra_fields.setdefault("is_superuser", True)
        return self._create_user(name, email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):

    GENDER = (
        ('F', 'female'),
        ('M', 'male'),
    )

    ROLES_USER = (
        ('ADMIN', 'Admin'),
        ('NORMAL', 'Normal'),
        ('SELLER', 'Seller'),
        ('CLIENT', 'Client')
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    gender = models.CharField(max_length=2, choices=GENDER, null=True)
    role = models.CharField(max_length=50, choices=ROLES_USER, default='NORMAL')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["name"]

    objects = CustomUserManager()
