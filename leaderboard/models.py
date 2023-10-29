from django.db import models
from users.models import User
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Display(models.Model):
    nickname = models.CharField(max_length=20)
    akun = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    