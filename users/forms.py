from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'password','role')