from django.http import JsonResponse
from django.shortcuts import render
from products.models import Product, Category, RecentlyViewed
from django.core.paginator import Paginator


from django.db import models

# ================= AUTOCOMPLETE =================

def autocomplete(request):
    q = request.GET.get('q', '').strip()
    if not q:
        return JsonResponse([], safe=False)

    products = Product.objects.prefetch_related('images').filter(
        models.Q(name__icontains=q) |
        models.Q(description__icontains=q) |
        models.Q(category__name__icontains=q)
    )[:6]

    data = []
    for p in products:
        img_url = ""
        if p.images.exists():
            img_url = p.images.first().image.url
        elif p.image_url:
            img_url = p.image_url

        data.append({
            "id": p.id,
            "name": p.name,
            "price": str(p.price),
            "category": p.category.name if p.category else "",
            "image": img_url
        })

    return JsonResponse(data, safe=False)


from products.views import home

# ================= SEARCH + FILTER + AUTO RECOMMEND =================

def search_results(request):
    return home(request)
