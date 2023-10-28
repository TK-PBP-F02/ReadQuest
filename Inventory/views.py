from django.shortcuts import render, redirect
from .models import Inventory, InventoryBook, Book
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist

def user_inventory(request):
    user=request.user
    user_inventories = None

    if user.is_authenticated:
        if user.role == "PENGGUNA":
            user_inventories = Inventory.objects.filter(user=user)
    return render(request, 'inventory.html', {'user_inventories': user_inventories})

def get_inventory_json(request):
    inventory_item = Inventory.objects.all()
    return HttpResponse(serializers.serialize('json', inventory_item))

@login_required
def create_folder(request):
    if request.method == 'POST':
        user = request.user
        name = request.POST.get("name")

        # print(name)
        new_product = Inventory.objects.create(user=user, name=name)

        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()

def login_users(request):
    return render(request, 'users/login.html', {})

def get_books_in_inventory(request, inventory_name):
    try:
        inventory = Inventory.objects.get(name=inventory_name, user=request.user)
    except ObjectDoesNotExist:
        return JsonResponse([], safe=False)  # Mengembalikan JSON kosong jika inventaris tidak ditemukan

    # Ambil semua buku dalam inventaris
    books = InventoryBook.objects.filter(inventory=inventory)

    # Siapkan data buku
    book_data = [
        {
            'title': book.book.title,
            'author': book.book.author,
            'description': book.book.description
        } for book in books
    ]

    return JsonResponse(book_data, safe=False)
