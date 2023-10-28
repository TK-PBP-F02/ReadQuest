# urls.py
from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    # Your existing URL patterns
    path('search/', views.search_books, name='search_books'),
    path('add-books/', views.add_books, name='add_books'),
    path('remove-book/', views.remove_book, name='remove_book'),
    path('', views.display_all_books, name='display_all_books'),
    path('books-dataset/', views.books_dataset, name='books_dataset'),
    path('book-detail/<int:pk>/', views.book_detail, name='book_detail'),
    path('book-act/<int:pk>/', views.book_act, name='book_act'),
]
