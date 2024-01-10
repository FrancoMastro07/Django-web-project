from django.shortcuts import render
from cart.cart import Cart

def home(request):
    
    cart = Cart(request)
    return render(request, "webProjectApp/home.html")





