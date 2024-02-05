from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from flowershop.models import Product
from general.forms import RegistrationForm, CustomAuthenticationForm

from .forms import ProductFilterForm


def index(request):
    product_list = Product.objects.filter(counts__gt=0).order_by('-date')

    # Обработка фильтрации
    form = ProductFilterForm(request.GET)
    if form.is_valid():
        cleaned_data = form.cleaned_data

        country = cleaned_data.get('country', '')
        name = cleaned_data.get('name', '')
        price_min = cleaned_data.get('price_min', None)
        price_max = cleaned_data.get('price_max', None)
        category = cleaned_data.get('category', '')

        if country:
            product_list = product_list.filter(country__name__icontains=country)
        if name:
            product_list = product_list.filter(name__icontains=name)
        if price_min is not None:
            product_list = product_list.filter(price__gte=price_min)
        if price_max is not None:
            product_list = product_list.filter(price__lte=price_max)
        if category:
            product_list = product_list.filter(category__name__icontains=category)

    return render(request, 'index.html', context={'product_list': product_list, 'form': form})


def product(request, product_id):
    product = Product.objects.get(id=product_id)

    return render(request, 'product.html', context={'product': product})


def about(request):
    new_products = Product.objects.order_by('-date')[:5]  # Получаем первые пять новинок
    return render(request, 'about.html', {'new_products': new_products})


def contact(request):
    return render(request, 'contact.html')


def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # Замените 'home' на имя вашего представления для перенаправления после входа
    else:
        form = CustomAuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')  # Замените 'home' на имя вашей домашней страницы
    else:
        form = RegistrationForm()

    return render(request, 'registration/register.html', {'form': form})
