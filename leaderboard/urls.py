from django.urls import path

app_name = 'leaderboard'

urlpatterns = [
    path('', show_main, name='show_main'),
]