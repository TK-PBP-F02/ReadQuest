from django.db import models

class Book(models.Model):
    isbn = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    publication_date = models.CharField(max_length=100)
    page_count = models.IntegerField()
    category = models.CharField(max_length=255)
    image_url = models.URLField()
    lang = models.CharField(max_length=100)
    readed = models.IntegerField(default=0)
    buys = models.IntegerField(default=0)
    quest_amount = models.IntegerField(default=0)
