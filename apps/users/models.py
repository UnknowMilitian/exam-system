from django.db import models
from django.contrib.auth.models import AbstractUser

from apps.users.managers import UserManager


class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name="Email")
    birth_date = models.DateField(verbose_name="Birth Date", null=True, blank=True)
    is_active = models.BooleanField(default=False, verbose_name="Is Active")
    is_staff = models.BooleanField(default=False, verbose_name="Is Staff")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
