from django.db import models

# Create your models here.

class lboard(models.Model):
    userName = models.CharField(max_length=255)
    points = models.IntegerField()
    

