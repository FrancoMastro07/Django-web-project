from django.shortcuts import render, HttpResponse

def home(request):
    return render(request, "webProjectApp/home.html")

def store(request):
    return render(request, "webProjectApp/store.html")

def contact(request):
    return render(request, "webProjectApp/contact.html")

