from django.shortcuts import render, redirect
from .forms import ContactForm

def contact(request):
    contactForm = ContactForm()
    if request.method == "POST":
        contactForm = ContactForm(data=request.POST)
        if contactForm.is_valid():
            name = request.POST.get("name")
            email = request.POST.get("email")
            content = request.POST.get("content")
            return redirect("/contact/?valid")
    return render(request, "contact/contact.html", {"contactForm":contactForm})
