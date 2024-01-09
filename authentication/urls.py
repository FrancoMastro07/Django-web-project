from django.urls import path
from .views import ViewRegistration

urlpatterns = [
    path('', ViewRegistration.as_view(), name="Authentication"),
]