from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render

from flowershop.models import Product


def index(request):
    product = Product.objects.filter(counts__gt=0)
    return render(request, 'index.html', context={'product': product})


def product(request, product_id):
    product = Product.objects.get(id=product_id)

    return render(request, 'product.html', context={'product': product})


def about(request):
    new_products = Product.objects.order_by('-date')[:5]  # Получаем первые пять новинок
    return render(request, 'about.html', {'new_products': new_products})


def contact(request):
    return render(request, 'contact.html')