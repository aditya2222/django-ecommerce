from django.shortcuts import render
from .models import Product
from django.views.generic import ListView,DetailView


# Create your views here.


class ProductListView(ListView):
    queryset = Product.objects.all()



class ProductDetailView(DetailView):
    model = Product
