from django.urls import path
from .views import *

urlpatterns = [
    # Your existing URL patterns
    path('', show_all_forum, name='forum'),
    path('books/<int:id>/', show_forum_per_book, name='forum'),
    path('<int:id>/', forum_detail, name='forum'),
    path('delete_forum', show_all_forum, name='forum'),
    path('delete_replies', show_all_forum, name='forum'),


]