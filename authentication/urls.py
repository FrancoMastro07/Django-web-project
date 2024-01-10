from django.urls import path
from .views import ViewRegistration, log_out, log_in

urlpatterns = [
    path('', ViewRegistration.as_view(), name="Authentication"),
    path('log_out', log_out, name="Logout"),
    path('log_in', log_in, name="Login"),
]