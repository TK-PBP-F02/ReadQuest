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
    path('user/json-all/', views.view_json_user, name='user_json'),
    path('login-flutter/', views.login_flutter, name='login_flutter'),
]
