from django.shortcuts import render, redirect
from .models import Cart
from products.models import Product


# Create your views here.


def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    products = cart_obj.products.all()
    total = 0
    for x in products:
        total += x.price
    print(total)
    cart_obj.total = total
    cart_obj.save()
    return render(request, 'carts/home.html', {})


def cart_update(request):
    product_obj = Product.objects.get(id=16)
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    if cart_obj in cart_obj.products.all():
        cart_obj.products.remove(product_obj)
    else:
        cart_obj.products.add(product_obj)
    # return redirect(product_obj.get_absolute_url())
    return redirect("carts:home")
