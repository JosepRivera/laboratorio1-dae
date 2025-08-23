# src/core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Original HTML view
    path('', views.item_list, name='item_list'),
    
    # API endpoints
    path('api/items/', views.api_items, name='api_items'),
    path('api/items/create/', views.api_create_item, name='api_create_item'),
]