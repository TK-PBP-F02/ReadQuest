from django.urls import path
from leaderboard.views import *


app_name = 'leaderboard'

urlpatterns = [
    
    path('leaderboard/', show_board, name='leaderboard'),
    path('leaderboard/regboard/',register_leaderboard, name='regboard'),
    path('leaderboard/delete/',clear_nickname_data,name='clear'),
    path('leaderboard/addpoint/',add_point,name='add_point'),
]