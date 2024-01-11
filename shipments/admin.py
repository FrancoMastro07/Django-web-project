from django.contrib import admin
from .models import Shipment, ShipmentLine

admin.site.register([Shipment, ShipmentLine])


