from django.http import HttpResponse
from django.shortcuts import render
import requests
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from Inventory.models import Inventory, InventoryBook
from users.views import custom_login
from quest.views import roler

# Create your views here.

api = 'AIzaSyDXkWtSpUh78YnFk1AFNBvszdmxffY2nEI'

def add_books_from_google_books_api(query, api_key):
    url = f'https://www.googleapis.com/books/v1/volumes?q={query}&key={api_key}'
    response = requests.get(url)
    data = response.json()

    if 'items' in data:
        
        for item in data['items']:
            if len(Book.objects.all()) >= 100 :
                return
            book_info = item.get('volumeInfo', {})
            title = book_info.get('title', '')
            author = ', '.join(book_info.get('authors', []))
            description = book_info.get('description', '')
            published_date = book_info.get('publishedDate', '')
            thumbnail = book_info['imageLinks']['thumbnail'] if 'imageLinks' in book_info else ''

            # Save the book to the database
            Book.objects.create(
                title=title,
                author=author,
                description=description,
                published_date=published_date,
                thumbnail=thumbnail
            )

def add_books(request):
    user = request.user
    if request.method == 'POST':
        query = request.POST.get('query', '')  # Retrieve the query from the form
        api_key = 'AIzaSyDXkWtSpUh78YnFk1AFNBvszdmxffY2nEI'

        # Add books based on the query using add_books_from_google_books_api function
        add_books_from_google_books_api(query, api_key)
    return render(request, 'add_books.html', {'username':user.username, 'role':roler(request)})


def display_all_books(request):
    books = Book.objects.all()
    user = request.user
    if user.is_anonymous:
        user = "none"
        return render(request, 'book.html', {'books': books, 'user':user, 'role':'not login'})
    elif user.role == "PENGGUNA":
        username = user.username
        point = user.point
        return render(request, 'book.html', {'books': books, 'username':username, 'point':point, 'role':'pengguna'})
    elif user.role == "ADMIN" :
        username = user.username
        return render(request, 'book.html', {'books': books, 'username':username, 'role':'admin'})
    return render(request, 'book.html', {'books': books, 'username' : user.username, 'role':'none'})

def books_dataset(request):
    books = Book.objects.all()
    return render(request, 'books.html', {'books': books})

from django.shortcuts import render, get_object_or_404
from .models import Book

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    user=request.user
    user_inventories = None

    if user.is_authenticated:
        if user.role == "PENGGUNA":
            print("wesss")
            user_inventories = Inventory.objects.filter(user=user)
    return render(request, 'book_detail.html', {'book': book, 'user_inventories': user_inventories, 'role':roler(request)})


def remove_book(request):
    user = request.user
    if request.method == 'POST':
        pk = request.POST.get('pk', None)
        if pk is not None:
            book = get_object_or_404(Book, pk=pk)
            book.delete()
    return render(request, 'remove_book.html', {'username':user.username, 'role':roler(request)})

def search_books(request):
    user = request.user
    if 'q' in request.GET:
        query = request.GET['q']
        results = Book.objects.filter(title__icontains=query)
    else:
        results = None
    role = 'none'
    if user.is_anonymous:
        return render(request, 'search_result.html', {'results': results, 'q':query, 'username':user.username, 'role':role})
    if user.role == "PENGGUNA":
        role = 'pengguna'
    elif user.role == "ADMIN":
        role = 'admin'
    return render(request, 'search_result.html', {'results': results, 'q':query, 'username':user.username, 'role':role})

def add_book_to_inventory(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    user = request.user

    if request.method == 'POST':
        folder_id = request.POST.get('folder')

        # Validasi apakah pengguna yang sedang masuk memiliki hak akses ke folder ini
        folder = get_object_or_404(Inventory, pk=folder_id)

        if folder.user == user:
            # Pastikan buku belum ada di dalam folder
            if not InventoryBook.objects.filter(inventory=folder, book=book).exists():
                # Tambahkan buku ke dalam folder inventory
                inventory_book = InventoryBook.objects.create(inventory=folder, book=book)
                # Tambahkan logika lain sesuai kebutuhan Anda
                return redirect('books:book_detail', pk=book_id)  # Redirect ke halaman detail buku
            # else:
                # Buku sudah ada dalam folder
                # Tambahkan logika atau pesan kesalahan yang sesuai
        # else:
            # Pengguna tidak memiliki hak akses ke folder ini
            # Tambahkan logika atau pesan kesalahan yang sesuai
    # Handle situasi ketika request bukan POST
    return redirect('books:book_detail', pk=book_id)  # Redirect kembali ke halaman detail buku