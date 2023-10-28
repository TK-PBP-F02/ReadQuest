from django.shortcuts import redirect, render
import requests
from django.shortcuts import render
from users.models import User
from django.urls import reverse
from leaderboard.models import Display
from django.contrib import messages  
from leaderboard.forms import ProductForm
from django.shortcuts import render, HttpResponseRedirect, reverse


# Create your views here.

def show_board(request):
    lboard_data= Display.objects.all()
    context = {
        'lboard_data' : lboard_data,
    }
    return render(request, 'mainboard.html', context)

def register_leaderboard(request):
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('leaderboard:leaderboard'))

    context = {'form':form}
    return render(request,'regboard.html', context)

def clear_nickname_data(request):
    Display.objects.all().delete()
    messages.success(request, "Nickname data has been cleared.")
    return HttpResponseRedirect(reverse('leaderboard:leaderboard'))
    
