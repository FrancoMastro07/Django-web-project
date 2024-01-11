from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Shipment, ShipmentLine
from cart.cart import Cart

@login_required(login_url="/authentication/log_in")
def process_shipment(request):
    shipment = Shipment.objects.create(user=request.user)
    cart = Cart(request)
    shipment_lines = list()
    for key, value in cart.cart.items():
        shipment_lines.append(ShipmentLine(
            
            product_id = key,
            amount = value["amount"],
            user = request.user,
            shipment = shipment
            
        ))
    ShipmentLine.objects.bulk_create(shipment_lines)
    send_mail(
            
        shipment = shipment,
        shipment_lines = shipment_lines,
        username = request.username,
        useremail = request.useremail
    
    )
    messages.success(request, "The order has been successfully created")
    return redirect("../store")

def send_mail():
    pass


