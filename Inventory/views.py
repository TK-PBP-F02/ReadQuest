from django.shortcuts import render, redirect
from .models import Inventory, InventoryBook
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.core import serializers
from django.urls import reverse
from django.views.decorators.http import require_POST
from quest.views import roler

def roler(request):
    user = request.user
    role = 'none'
    if user.role == "PENGGUNA":
        role = 'pengguna'
    elif user.role == "ADMIN":
        role = 'admin'
    return role

def user_inventory(request):
    user=request.user
    user_inventories = None
    role = None

    if user.is_authenticated:
        user_inventories = Inventory.objects.filter(user=user)
        role = roler(request)
    return render(request, 'inventory.html', {'user_inventories': user_inventories, 'role' : role})

def get_inventory_json(request):
    inventory_item = Inventory.objects.all()
    return HttpResponse(serializers.serialize('json', inventory_item))

@login_required
def create_folder(request):
    if request.method == 'POST':
        user = request.user
        name = request.POST.get("name")
        new_product = Inventory.objects.create(user=user, name=name)

        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()

@require_POST
def delete_book(request, book_id):
    book = InventoryBook.objects.get(id=book_id)

    if book.inventory.user == request.user:
        book.delete()

    return HttpResponseRedirect(reverse('Inventory:user_inventory'))

def view_json_inventory(request, pk):
    data = Inventory.objects.filter(user=pk)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def view_json_inventory_book(request):
    data = InventoryBook.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def view_json_inventory_book_id(request, pk):
    data = InventoryBook.objects.filter(inventory=pk)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")