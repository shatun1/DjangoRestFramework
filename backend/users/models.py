from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    password = models.CharField(max_length=32)
    birthday_year = models.PositiveIntegerField()
    email = models.CharField(max_length=64, unique=True)
