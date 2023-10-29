from django.urls import path, include
from make_journey_jurnal.views import create_book, display_all_books, book_detail_make, delete_book_make

app_name = 'make_journey_jurnal'

urlpatterns = [
    path('create-book/', create_book, name='create_book'),
    path('display-all-books/', display_all_books, name='display_all_books'),
    path('book-detail-make/<int:pk>/',book_detail_make, name='book_detail_make'),
    path('delete-book-make/', delete_book_make, name='delete_book_make'),
    ]