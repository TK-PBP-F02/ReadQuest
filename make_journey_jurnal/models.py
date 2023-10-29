from django.db import models

# Create your models here.
class Book(models.Model):
    isbn = models.CharField(max_length=100, default = '')
    title = models.CharField(max_length=255, default = '')
    description = models.TextField()
    author = models.CharField(max_length=255, default ='')
    publisher = models.CharField(max_length=255, default = '')
    publication_date = models.CharField(max_length=100, default='')
    page_count = models.IntegerField(default=0)
    category = models.CharField(max_length=255, default ='')
    image_url = models.URLField()
    lang = models.CharField(max_length=100, default='')
    #readed = models.IntegerField(default=0)
    #buys = models.IntegerField(default=0)