# from django.test import TestCase

# # Create your tests here.
# # from django.test import TestCase
# from .views import add_books_from_google_books_api
# from .models import Book

# class GoogleBooksAPITest(TestCase):
#     def test_add_books_from_google_books_api(self):
#         # Buat beberapa data palsu yang akan digunakan dalam pengujian
#         query = "Harry Potter"  # Ganti dengan query yang sesuai
#         api_key = 'AIzaSyDXkWtSpUh78YnFk1AFNBvszdmxffY2nEI'

#         # Panggil fungsi yang akan diuji
#         add_books_from_google_books_api(query, api_key)

#         # Pastikan bahwa beberapa buku telah ditambahkan ke database
#         books_count = Book.objects.filter(title__icontains=query).count()
#         self.assertGreater(books_count, 0)
