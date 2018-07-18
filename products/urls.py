from django.urls import path,include
from .views import ProductListView,ProdcutDetailSlugView


app_name = 'products'
urlpatterns = [
    path('', ProductListView.as_view(), name='list'),
    path('<slug:slug>/', ProdcutDetailSlugView.as_view(), name='details'),
]