import json
from django.shortcuts import get_object_or_404, render, redirect

from books.models import Book
from .models import Inventory, InventoryBook
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.urls import reverse
from django.views.decorators.http import require_POST
from quest.views import roler
from django.views.decorators.csrf import csrf_protect


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
@csrf_protect
def create_folder(request):
    if request.method == 'POST':
        user = request.user
        name = request.POST.get("name")
        new_product = Inventory.objects.create(user=user, name=name)

        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()

@require_POST
@csrf_protect
def delete_book(request, book_id):
    book = InventoryBook.objects.get(id=book_id)

    if book.inventory.user == request.user:
        book.delete()

    return HttpResponseRedirect(reverse('Inventory:user_inventory'))

def view_json_inventory(request):
    user=request.user
    data = None
    data = Inventory.objects.filter(request.user.pk)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def view_json_inventory_book(request):
    user = request.user
    user_inventories = Inventory.objects.filter(user=user)
    data = InventoryBook.objects.filter(inventory__in=user_inventories)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def view_json_inventory_book_id(request, id):
    user = request.user
    try:
        inventory = Inventory.objects.get(user=user, id=id)
        data = InventoryBook.objects.filter(inventory=inventory)
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    except Inventory.DoesNotExist:
        return HttpResponseNotFound("Inventory not found")

@csrf_exempt
def create_inventory_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        inventory_data_str = json.dumps(data.get('Inventory.inventory', []))
        if inventory_data_str:
            inventory_data = json.loads(inventory_data_str)
            if inventory_data:
                inventory_entry = inventory_data[0]
                name = inventory_entry.get("fields").get("name")
                if name is not None:
                    existing_inventory = Inventory.objects.filter(user=request.user, name=name).first()
                    if existing_inventory:
                        return JsonResponse({"status": "exist"}, status=200)
                    
                    new_inventory = Inventory.objects.create(
                        user=request.user,
                        name=name,
                    )

                    new_inventory.save()

                    return JsonResponse({"status": "success"}, status=200)
    
    else:
        return JsonResponse({"status": "error"}, status=401)
    
@csrf_exempt
def delete_inventory_flutter(request, book_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        inventory_data_str = json.dumps(data.get('Inventory.inventorybook', []))
        if inventory_data_str:
            inventory_data = json.loads(inventory_data_str)
            if inventory_data:
                inventory_entry = inventory_data[0]
                this_inventory = inventory_entry.get("fields")
                inventory_id = this_inventory.get('inventory')
                inventory = get_object_or_404(Inventory, pk=inventory_id)
                if InventoryBook.objects.filter(inventory=inventory, book=book_id).exists():
                    inventory_book = InventoryBook.objects.get(inventory=inventory, book=book_id)
                    inventory_book.delete()
                    return JsonResponse({"status": "success"}, status=200)
                else:
                    return JsonResponse({"status": "exist"}, status=200)

    else:
        return JsonResponse({"status": "error"}, status=401)