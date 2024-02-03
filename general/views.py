from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render

from flowershop.models import Product


def index(request):
    product = Product.objects.filter(counts__gt=0)
    return render(request, 'index.html', context={'product': product})


def product(request, product_id):
    product = Product.objects.get(id=product_id)

    return render(request, 'product.html', context={'product': product})


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'


class CustomLogoutView(LogoutView):
    template_name = 'registration/logout.html'


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')