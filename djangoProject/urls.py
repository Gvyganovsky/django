from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include

from django.contrib.auth.views import LoginView, LogoutView

from general import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('product/<int:product_id>', views.product),

    # path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    # path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),

    path('accounts/', include('django.contrib.auth.urls')),

    path('', views.index)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
