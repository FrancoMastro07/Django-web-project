from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
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
    send_email(
            
        shipment = shipment,
        shipment_lines = shipment_lines,
        username = request.user.username,
        useremail = request.user.email
    
    )
    messages.success(request, "The order has been successfully created")
    return redirect("../store")

def send_email(**kwargs):
    issue = "Thanks for the order"
    message = render_to_string("emails/shipment.html",{
        
        "shipment": kwargs.get("shipment"),
        "shipment_lines": kwargs.get("shipment_lines"),
        "username": kwargs.get("username")
        
    })
    text_message = strip_tags(message)
    from_email = "webprojectdjango@gmail.com"
    to = kwargs.get("useremail")
    send_mail(issue, text_message, from_email, [to], html_message=message)
    

