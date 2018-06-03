from django.urls import path,include
from .views import ProductListView, ProductDetailView


app_name = 'products'
urlpatterns = [
    path('', ProductListView.as_view(), name='list'),
    path('<slug:slug>', ProductDetailView.as_view(), name='details'),
]