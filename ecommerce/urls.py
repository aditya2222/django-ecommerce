"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from products.views import HomePageView, BootstrapView
from django.contrib.auth.views import LogoutView
from accounts.views import guest_register_view
from addresses.views import checkout_address_create_view, checkout_address_reuse_view

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('guest/register', guest_register_view, name='guest_register'),
    path('products/', include('products.urls', namespace='products')),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('bootstrap/', BootstrapView.as_view(), name='bootstrap'),
    path('search/', include('search.urls', namespace='search')),
    path('cart/', include('carts.urls', namespace='cart')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('checkout/address/create/', checkout_address_create_view, name='checkout_address_create'),
    path('checkout/address/reuse/', checkout_address_reuse_view, name='checkout_address_reuse'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
