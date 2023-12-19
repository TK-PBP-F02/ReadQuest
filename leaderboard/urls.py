from django.urls import path
from leaderboard.views import *


app_name = 'leaderboard'

urlpatterns = [
    
    path('leaderboard/', show_board, name='leaderboard'),
    path('leaderboard/regboard/',register_leaderboard, name='regboard'),
    path('leaderboard/delete/',clear_nickname_data,name='clear'),
    path('leaderboard/addpoint/',add_point,name='add_point'),
    path('leaderboard/all-json/', all_json, name='all_json'),
    path('leaderboard/user-json/', user_json, name = 'user_json'),
    path('leaderboard/regboard-flutter/',reg_leaderboard_flutter, name='regboard_flutter'),
]