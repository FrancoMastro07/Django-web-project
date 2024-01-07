from django.shortcuts import redirect
from .cart import Cart
from store.models import Product

def add(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.add(product=product)
    return redirect("store")

def delete(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.delete(product=product)
    return redirect("store")

def subtract_product(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.subtract_product(product=product)
    return redirect("store")

def cart_clean(request):
    cart = Cart(request)
    cart.subtract_product()
    return redirect("store")


