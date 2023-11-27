# urls.py
from django.urls import path
from . import views

app_name = 'quest'

urlpatterns = [
    # Your existing URL patterns
    path('quest/', views.view_quest, name='quest'),
    path('quest/create/', views.create_quest, name='quest_create'),
    path('quest/delete/', views.delete_quest, name='quest_delete'),
    path('quest/<int:id>/', views.quest_detail, name='quest_detail'),
    path('quest-book-detail/<int:pk>/', views.quest_book_detail, name='quest_book_detail'),
    path('quest/json-all/', views.view_json_quest, name='view_json_quest'),
]
