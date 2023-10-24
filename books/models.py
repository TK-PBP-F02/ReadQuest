from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    published_date = models.TextField()
    thumbnail = models.URLField()
    readed = models.IntegerField(default=0)