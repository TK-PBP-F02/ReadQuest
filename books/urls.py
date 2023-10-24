# urls.py
from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    # Your existing URL patterns
    path('add-books/', views.add_books, name='add_books'),
    path('remove-book/', views.remove_book, name='remove_book'),
    path('books/', views.display_all_books, name='display_all_books'),
]
