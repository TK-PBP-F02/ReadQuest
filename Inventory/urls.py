from django.urls import path, include
# from Inventory.views import add_book_to_inventorys
from . import views

app_name = 'Inventory'

urlpatterns = [
    # path('', show_inventory, name='show_inventory'),
    # path('ReadQuest/', include('ReadQuest.urls')), # hubungin ke main (?)
    # path('', views.add_book_to_inventory, name='add_book_to_inventory'),
    path('add-book/', views.add_book_to_inventory, name='add_book_to_inventory'), # Ubah 'name' menjadi 'add_book_to_inventory'
    path('coba/', views.coba, name='coba'), # Ubah 'name' menjadi 'coba'
]