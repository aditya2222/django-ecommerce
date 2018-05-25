from django.shortcuts import render
from .models import Cart


# Create your views here.


def CartsView(request):
    cart_obj = Cart.objects.new_or_get(request)
    return render(request, 'carts/home.html', {})
