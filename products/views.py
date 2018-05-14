from django.shortcuts import render
from .models import Product
from django.views.generic import ListView, DetailView, TemplateView, CreateView
from .forms import UserCreationForm
from django.urls import reverse_lazy


# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home_page.html'


class ProductListView(ListView):

    def get_queryset(self):
        return Product.objects.all()


class ProductDetailView(DetailView):
    model = Product


class CreateUserView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
