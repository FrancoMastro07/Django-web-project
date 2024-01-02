from django.shortcuts import render

def home(request):
    return render(request, "webProjectApp/home.html")

def store(request):
    return render(request, "webProjectApp/store.html")



