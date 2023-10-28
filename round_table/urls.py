from django.urls import path
from .views import *

app_name = 'round_table'

urlpatterns = [
    # Your existing URL patterns
    path('', show_all_forum, name='show_all_forum'),
    path('add-forum/', add_forum, name='add_forum'),
    path('add-reply/<int:id>/', add_reply, name='add_reply'),
    path('<int:id>/', forum_detail, name='forum_detail'),
    path('delete-forum/<int:id>/', delete_forum, name='delete_forum'),
    path('delete-reply/<int:id>/', delete_reply, name='delete_reply'),
    path('search/', search_forums, name='search_forums'),
]