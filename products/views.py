from django.shortcuts import render
from .models import Product
from django.views.generic import ListView, DetailView, TemplateView, CreateView
from .forms import UserCreationForm
from django.urls import reverse_lazy
from carts.models import Cart


# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home_page.html'


class ProductListView(ListView):

    def get_queryset(self):
        return Product.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context


class ProductDetailView(DetailView):
    model = Product


class BootstrapView(TemplateView):
    template_name = 'bootstrap/example.html'


class ProdcutDetailSlugView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/product_detail.html"

    def get_context_data(self, **kwargs):
        context = super(ProdcutDetailSlugView, self).get_context_data(**kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context

# def get_context_data(self, **kwargs):
#     context = super().get_context_data(**kwargs)
#     context['number'] = random.randrange(1, 100)
#     return context
