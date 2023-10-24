from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    class Role(models.TextChoices):
        PENGGUNA = "PENGGUNA", 'Pengguna'
        ADMIN = "ADMIN", 'Admin'

    role = models.CharField(max_length=20, default='Pengguna', choices=Role.choices)