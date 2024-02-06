from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    patronymic = models.CharField(max_length=100)
    rules = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.password:
            self.password = make_password(self.password)  # Хешируем пароль перед сохранением
        super().save(*args, **kwargs)

    def get_cart(self):
        # Возвращает корзину пользователя
        cart, created = Cart.objects.get_or_create(user=self)
        return cart


class Category(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return f"{self.name} (id: {self.id})"


class Country(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return f"{self.name} (id: {self.id})"


class Product(models.Model):
    name = models.CharField(max_length=80)
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to='products')  # Создаст папку products внутри папки media
    date = models.DateTimeField()
    counts = models.PositiveIntegerField()
    color = models.CharField(max_length=60)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} (id: {self.id})"


class Cart(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)

    def calculate_total_price(self):
        return sum(product.price for product in self.products.all())


class Order(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - {self.user.username}"
