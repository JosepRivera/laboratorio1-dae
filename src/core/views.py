# src/core/views.py
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
from .models import Item

def home(request):
    """Renderiza el frontend index.html"""
    return render(request, "core/item_list.html")

# API Endpoints
def api_items(request):
    """GET: Return all items as JSON"""
    items = Item.objects.all()
    items_data = [
        {
            'id': item.id,
            'name': item.name,
            'description': item.description,
            'created_at': item.created_at.isoformat()
        }
        for item in items
    ]
    return JsonResponse({'items': items_data})

@csrf_exempt
@require_http_methods(["POST"])
def api_create_item(request):
    """POST: Create a new item"""
    try:
        data = json.loads(request.body)
        item = Item.objects.create(
            name=data.get('name', ''),
            description=data.get('description', '')
        )
        return JsonResponse({
            'id': item.id,
            'name': item.name,
            'description': item.description,
            'created_at': item.created_at.isoformat()
        }, status=201)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)