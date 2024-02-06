from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include

from django.contrib.auth.views import LoginView, LogoutView

from general import views
from general.views import index, login_view, view_cart, checkout, add_to_cart, remove_from_cart

urlpatterns = [
    path('admin/', admin.site.urls),

    path('product/<int:product_id>', views.product),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),

    path('about/', views.about),
    path('contact/', views.contact),

    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('remove-from-cart/<int:product_id>/', remove_from_cart, name='remove_from_cart'),

    path('', index, name='index')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
