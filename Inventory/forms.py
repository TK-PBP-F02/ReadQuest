from django.forms import ModelForm
from Inventory.models import Inventory

class ProductForm(ModelForm):
    class Meta:
        model = Inventory
        fields = ["name"]