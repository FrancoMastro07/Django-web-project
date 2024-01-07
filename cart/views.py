from django.shortcuts import redirect
from .cart import Cart
from store.models import Product

def add_product(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.add(product=product)
    return redirect("Store")

def delete_product(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.delete(product=product)
    return redirect("Store")

def subtract_product(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.subtract(product=product)
    return redirect("Store")

def cart_clean(request):
    cart = Cart(request)
    cart.clean()
    return redirect("Store")


