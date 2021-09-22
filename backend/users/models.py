from django.db import models
# from django.contrib.auth.base_user import BaseUserManager

from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.CharField(max_length=128, unique=True)
