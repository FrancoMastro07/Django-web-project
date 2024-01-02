from django.shortcuts import render
from .forms import ContactForm

def contact(request):
    contactForm = ContactForm()
    return render(request, "contact/contact.html", {"contactForm":contactForm})
