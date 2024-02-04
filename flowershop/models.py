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
