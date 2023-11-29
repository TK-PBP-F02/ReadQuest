from django.db import models
from django.contrib.auth.models import AbstractUser, User

class Role(models.TextChoices):
        PENGGUNA = "PENGGUNA", 'Pengguna'
        ADMIN = "ADMIN", 'Admin'

class User(AbstractUser):
    base_role = Role.PENGGUNA
    point = models.IntegerField(default=0)
    readed = models.IntegerField(default=0)
    buyed = models.IntegerField(default=0)
    reviewed = models.IntegerField(default=0)
    role = models.CharField(max_length=20, choices=Role.choices)
    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs)

class Admin(User):
    base_role = Role.ADMIN
    class Meta:
         proxy = True