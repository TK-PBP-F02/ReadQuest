from django.db import models
from users.models import User
from books.models import Book

class Forum(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True)

class Replies(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    parent_forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    content = models.TextField(max_length=5000) 
    created_at = models.DateTimeField(auto_now_add=True)