from django.shortcuts import render
from .models import Product
from django.views.generic import ListView


# Create your views here.


class ProductListView(ListView):
    queryset = Product.objects.all()
