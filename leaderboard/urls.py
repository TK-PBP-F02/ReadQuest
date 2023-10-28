from django.urls import path
from leaderboard.views import *

app_name = 'leaderboard'

urlpatterns = [
    path('leaderboard/', show_board, name='leaderboard'),
    path('leadearboard/regboard/',register_leaderboard, name='regboard'),
    path('leaderboard/',clear_nickname_data,name='clear'),
]