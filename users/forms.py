from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Admin, User

class AdminRegistrationForm(UserCreationForm):
    class Meta:
        model = Admin
        fields = ('username', 'password1', 'password2', 'email', 'is_staff')

class PenggunaRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email')