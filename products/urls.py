from django.urls import path
from .views import ProductListView, ProductDetailView,CreateUserView


app_name = 'products'
urlpatterns = [
    path('', ProductListView.as_view(), name='list'),
    path('register/', CreateUserView.as_view(), name='register'),
    path('<slug:slug>', ProductDetailView.as_view(), name='details'),
]