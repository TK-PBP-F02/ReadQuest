from django.shortcuts import render
import requests
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from leaderboard.models import lboard
# Create your views here.

def show_board(request):
    products = lboard.objects.filter(user=request.user)
    context = {
        'name': request.user.username,
        'products': products,
        'last_login': request.COOKIES['last_login'],
    }
    return render(request, "leaderboard.html", context)