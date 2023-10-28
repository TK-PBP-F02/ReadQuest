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
    path('get-forum/', get_forums_json, name='get_forums_json'),
    path('delete-forum-ajax/<int:id>/', delete_forum_ajax, name='delete_forum_ajax'),
    path('get-replies/', get_replies_json, name='get_replies_json'),
    path('<int:forum_id>/delete-reply-ajax/<int:reply_id>/', delete_reply_ajax, name='delete_reply_ajax'),
]