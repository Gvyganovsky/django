from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path

from general import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('product/<int:product_id>', views.product),

    path('', views.index)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
