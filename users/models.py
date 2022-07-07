from django.db import models
from django.contrib.auth.models import AbstractUser

from users.managers import UserManager


class User(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    updated_at = models.DateTimeField(auto_now=True)

    username = None

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = UserManager()
