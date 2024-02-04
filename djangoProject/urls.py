from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include

from django.contrib.auth.views import LoginView, LogoutView

from general import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('product/<int:product_id>', views.product),

    path('accounts/', include('django.contrib.auth.urls')),

    path('about/', views.about),
    path('contact/', views.contact),

    path('', views.index)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
