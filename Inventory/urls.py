from django.urls import path, include
from Inventory import views

app_name = 'Inventory'

urlpatterns = [
    path('', include('users.urls')),
    path('inventory', views.user_inventory, name='user_inventory'),
    path('get-inventory/', views.get_inventory_json, name='get_inventory_json'),
    path('create-folder/', views.create_folder, name='create_folder'),
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),
    path('inventory/json-inventory/', views.view_json_inventory, name='view_json_inventory'),
    path('inventory/json-inventory-books/', views.view_json_inventory_book, name='view_json_inventory_books'),
    path('inventory/json-inventory-books/<int:id>/', views.view_json_inventory_book_id, name='view_json_inventory_books_id'),

]
