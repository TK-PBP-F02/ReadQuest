from django.forms import ModelForm
from leaderboard.models import Display
from users.models import User

class ProductForm(ModelForm):
    class Meta:
        model = Display
        fields = ["nickname"]

    
