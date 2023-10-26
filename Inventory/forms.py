from django.forms import ModelForm
from users.models import User
from books.models import Book
from .models import UserInventory

class InventoryForm(ModelForm):
    class Meta:
        model = UserInventory
        fields = ["name", "price", "description"]