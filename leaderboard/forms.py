from django.forms import ModelForm
from leaderboard.models import form

class ProductForm(ModelForm):
    class Meta:
        model = form
        fields = ["name", "price", "description"]