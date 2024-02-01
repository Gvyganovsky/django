from django.contrib import admin
from flowershop.models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'image', 'date', 'counts', 'color', 'category', 'country')


admin.site.register(CustomUser)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Product, ProductAdmin)