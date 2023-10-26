from django.db import models
# from django.contrib.auth.models import User  # Import model User dari aplikasi "users"
from books.models import Book  # Import model Book dari aplikasi "books"

class UserInventory(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    read = models.BooleanField(default=False)