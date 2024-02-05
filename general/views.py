from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView

from flowershop.models import Product
from general.forms import RegisterForm

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


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
