from django.db import models
from users.models import User

class Book(models.Model):
<<<<<<< HEAD
    isbn = models.CharField(max_length=100)
=======
    def __str__(self):
        return self.title
    
>>>>>>> de4bcd25428db364305c5704d96e89ad195c3cec
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    published_date = models.TextField()
    thumbnail = models.URLField()
    readed = models.IntegerField(default=0)
    publisher = models.CharField(max_length=255)
    publication_date = models.CharField(max_length=100)
    page_count = models.IntegerField()
    category = models.CharField(max_length=255)
    image_url = models.URLField()
    lang = models.CharField(max_length=100)
    readed = models.IntegerField(default=0)
    buys = models.IntegerField(default=0)
    quest_amount = models.IntegerField(default=0)

class BookRead(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    date_read = models.DateTimeField(auto_now=True)

class BookBought(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    date_bought = models.DateTimeField(auto_now=True)

class BookReviewed(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    date_reviewed = models.DateTimeField(auto_now=True)