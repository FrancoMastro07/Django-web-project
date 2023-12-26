from django.urls import path
from webProjectApp import views

urlpatterns = [
    path('', views.home, name="Home"),
    path('services', views.services, name="Services"),
    path('store', views.store, name="Store"),
    path('blog', views.blog, name="Blog"),
    path('contact', views.contact, name="Contact"),
]