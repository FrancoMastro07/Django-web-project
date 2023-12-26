from django.shortcuts import render, HttpResponse

def home(request):
    return HttpResponse("Home")

def services(request):
    return HttpResponse("Services")

def store(request):
    return HttpResponse("Store")

def blog(request):
    return HttpResponse("Blog")

def contact(request):
    return HttpResponse("Contact")

