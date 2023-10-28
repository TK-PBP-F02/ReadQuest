from django.urls import path, include
from Inventory import views

app_name = 'Inventory'

urlpatterns = [
    path('', include('users.urls')),
    path('inventory', views.user_inventory, name='user_inventory'),
    path('get-inventory/', views.get_inventory_json, name='get_inventory_json'),
    path('create-folder/', views.create_folder, name='create_folder'),
    path('login-users', views.login_users, name='login_users'),
    path('get-books-in-inventory/<str:inventory_name>/', views.get_books_in_inventory, name='get_books_in_inventory'),
]
