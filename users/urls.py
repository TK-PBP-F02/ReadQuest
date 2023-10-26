# urls.py
from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    # Your existing URL patterns
    path('login/', views.custom_login, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/user', views.register_users, name='register_user'),
    path('register/admin', views.register_admin, name='register_admin'),
]
