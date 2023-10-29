from django.db import models
from books.models import Book
# Create your models here.


class QuestContainer(models.Model):
    book_key = models.ForeignKey(Book, on_delete=models.CASCADE)

class Quest(models.Model):
    name = models.CharField(max_length=23)
    desc = models.TextField()
    goal = models.CharField(max_length=100)
    point = models.IntegerField(default=10)
    type = models.CharField(max_length=100, default='WordlQuest')
    amount = models.IntegerField(default=1)
    book_id = models.IntegerField(default=0)
    container = models.ForeignKey(QuestContainer, on_delete=models.CASCADE, blank=True, null=True)