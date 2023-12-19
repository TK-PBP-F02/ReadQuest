import json
from django.http import HttpResponseNotFound, JsonResponse
from django.shortcuts import redirect, render
import requests
from django.shortcuts import render
from users.models import User as u
from django.contrib.auth.models import User
from django.urls import reverse
from leaderboard.models import Display
from django.contrib import messages  
from leaderboard.forms import ProductForm
from django.shortcuts import render, HttpResponseRedirect, reverse, HttpResponse
from quest.views import roler
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt



# Create your views here.


# Fungsi untuk memunculkan Leaderboard page
def show_board(request):
    akun_data = request.user
    lboard_data = Display.objects.all().order_by('-akun__point')
    if akun_data.is_anonymous:
        context = {
        'lboard_data' : lboard_data,
        'akun_data':akun_data,
        }
        return render(request, 'mainboard.html', context)

    specific_object = Display.objects.filter(akun=akun_data)
    context = {
        'lboard_data' : lboard_data,
        'role': roler(request),
        'akun_data':akun_data,
        'specific_object':specific_object,
    }
    return render(request, 'mainboard.html', context)

# Fungsi untuk memunculkan Register Leaderboard page
def register_leaderboard(request):
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST)
        akun = request.user
        if form.is_valid():
            nick = request.POST.get('nickname')
            # u.objects.filter(pk=akun.pk).update(form_submitted=True)
            display = Display(nickname=nick,akun=akun)
            display.save()
            return HttpResponseRedirect(reverse('leaderboard:leaderboard'))

    context = {
        'logged_in':request.user,
        'form':form,
        'role':roler(request),
    }
    return render(request,'regboard.html', context)

# Fungsi untuk clear leaderboard
def clear_nickname_data(request):
    Display.objects.all().delete()
    return HttpResponseRedirect(reverse('leaderboard:leaderboard'))

# Fungsi untuk add point (Gak kepake)
def add_point(request):
    logged = request.user
    data = Display.objects.get(akun=logged)
    uuuser = u.objects.get(username=logged)
    uuuser.point+=1
    uuuser.save()
    return HttpResponseRedirect(reverse('leaderboard:leaderboard'))


# Fungsi untuk add nickname (Gak kepake)
def add_nickname_ajax(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            akun = request.user
            nickname = request.POST.get("name")
            new_product = Display(nickname=nickname, akun=akun)
            new_product.save()
            return HttpResponse(b"CREATED", status=201)
        else:
            return HttpResponse(b"NOT FOUND", status=205)
    return HttpResponseNotFound()

def all_json(request):
    data = Display.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def user_json(request,id):
    data = u.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@csrf_exempt
def reg_leaderboard_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)

        new_Display = Display.objects.create(
            nickname = data["nickname"],
            akun = request.user,
        )

        new_Display.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)



