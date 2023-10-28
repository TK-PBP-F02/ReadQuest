from django.db import models

# Create your models here.

class Display(models.Model):
    nickname = models.CharField(max_length=20)


