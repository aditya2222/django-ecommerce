from django.shortcuts import render
from .models import Product
from django.views.generic import ListView, DetailView,TemplateView


# Create your views here.

class HomePageView(TemplateView):
	template_name = 'home_page.html'

class ProductListView(ListView):

    def get_queryset(self):
        return Product.objects.all()    	


class ProductDetailView(DetailView):
    model = Product



