from django.urls import path
from .views import ViewRegistration, log_out

urlpatterns = [
    path('', ViewRegistration.as_view(), name="Authentication"),
    path('log_out', log_out, name="Logout"),
]