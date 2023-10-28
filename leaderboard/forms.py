from django.forms import ModelForm
from leaderboard.models import Display

class ProductForm(ModelForm):
    class Meta:
        model = Display
        fields = ["nickname"]
