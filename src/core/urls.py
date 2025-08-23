from django.urls import path
from . import views

urlpatterns = [
    # Vista principal ahora será index.html
    path('', views.home, name='home'),

    # API endpoints
    path('api/items/', views.api_items, name='api_items'),
    path('api/items/create/', views.api_create_item, name='api_create_item'),
]
