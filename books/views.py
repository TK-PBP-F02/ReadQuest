from django.shortcuts import render
import requests
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book

# Create your views here.

api = 'AIzaSyDXkWtSpUh78YnFk1AFNBvszdmxffY2nEI'

def add_books_from_google_books_api(query, api_key):
    url = f'https://www.googleapis.com/books/v1/volumes?q={query}&key={api_key}'
    response = requests.get(url)
    data = response.json()

    if 'items' in data:
        for item in data['items']:
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
    if request.method == 'POST':
        query = request.POST.get('query', '')  # Retrieve the query from the form
        api_key = 'AIzaSyDXkWtSpUh78YnFk1AFNBvszdmxffY2nEI'

        # Add books based on the query using add_books_from_google_books_api function
        add_books_from_google_books_api(query, api_key)

    return render(request, 'add_books.html')


def display_all_books(request):
    books = Book.objects.all()
    return render(request, 'book.html', {'books': books})

def books_dataset(request):
    books = Book.objects.all()
    return render(request, 'books.html', {'books': books})

from django.shortcuts import render, get_object_or_404
from .models import Book

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book_detail.html', {'book': book})


def remove_book(request):
    if request.method == 'POST':
        pk = request.POST.get('pk', None)
        if pk is not None:
            book = get_object_or_404(Book, pk=pk)
            book.delete()

    return render(request, 'remove_book.html')

def search_books(request):
    if 'q' in request.GET:
        query = request.GET['q']
        results = Book.objects.filter(title__icontains=query)
    else:
        results = None
    return render(request, 'search_result.html', {'results': results, 'q':query})