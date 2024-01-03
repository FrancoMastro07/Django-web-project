from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import EmailMessage

def contact(request):
    contactForm = ContactForm()
    if request.method == "POST":
        contactForm = ContactForm(data=request.POST)
        if contactForm.is_valid():
            name = request.POST.get("name")
            email = request.POST.get("email")
            content = request.POST.get("content")
            email_send = EmailMessage("Message from contact app", "This message was sent by {} from this email: {} and describes:\n\n {}".format(name, email, content), "", ["webprojectdjango@gmail.com"], reply_to=[email])
            try:
                email_send.send()
                return redirect("/contact/?valid")
            except:
                return redirect("/contact/?invalid")
    return render(request, "contact/contact.html", {"contactForm":contactForm})
