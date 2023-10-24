# urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Your existing URL patterns
    path('login/', views.login, name='login'),
    path('register/', views.login, name='login'),
]
