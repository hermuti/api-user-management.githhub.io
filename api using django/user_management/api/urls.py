from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.list_users, name='list_users'),  # Handles GET requests
    path('users/', views.create_user, name='create_user'),  # Handles POST requests 
    path('users/<int:pk>/', views.delete_user, name='delete_user'), # Handles DELETE requests
]
