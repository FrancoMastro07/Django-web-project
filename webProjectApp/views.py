from django.shortcuts import render, HttpResponse

def home(request):
    return render(request, "webProjectApp/home.html")

def store(request):
    return render(request, "webProjectApp/store.html")

def blog(request):
    return render(request, "webProjectApp/blog.html")

def contact(request):
    return render(request, "webProjectApp/contact.html")

