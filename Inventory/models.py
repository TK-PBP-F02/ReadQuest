from django.db import models
from users.models import User
from books.models import Book

class Inventory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default="Inventory")

class InventoryBook(models.Model):
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)