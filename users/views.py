from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages  
from .forms import AdminRegistrationForm, PenggunaRegistrationForm
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib import messages
from django.core import serializers

# Create your views here.

from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib import messages
from quest.views import quest_point
from django.views.decorators.csrf import csrf_exempt
from users.models import User

@csrf_exempt
def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # Use Django's login function
            quest_point(request)
            response = HttpResponseRedirect(reverse("books:display_all_books"))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

@csrf_exempt
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('books:display_all_books'))
    return response

@csrf_exempt
def register_admin(request):
    form = AdminRegistrationForm()
    if request.method == "POST":
        form = AdminRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('user:login')
    context = {'form':form, 'link':'/register/user', 'role':'Admin', 'other_role':'User'}
    return render(request, 'register.html', context)

@csrf_exempt
def register_users(request):
    form = PenggunaRegistrationForm()
    if request.method == "POST":
        form = PenggunaRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('user:login')
    context = {'form':form, 'link':'/register/admin', 'role':'User', 'other_role':'Admin'}
    return render(request, 'register.html', context)

def view_json_user(request):
    data = User.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")