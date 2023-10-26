from django.shortcuts import render, redirect
from .models import Book

def add_book_to_inventory(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        description = request.POST.get('description')

        # Simpan buku ke dalam katalog
        Book.objects.create(title=title, author=author, description=description)

        return redirect('inventory')  # Ganti 'inventory' dengan URL katalog Anda

    return render(request, 'inventory.html')

def coba(request):
    context = {
        'name': 'Pak Bepe', # Nama kamu
        'class': 'PBP A', # Kelas PBP kamu
    }

    return render(request, "inventory.html", context)
