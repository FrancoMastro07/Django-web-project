from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import F, Sum, FloatField
from store.models import Product

User = get_user_model()

class Shipment(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id
        
    @property
    def total(self):
        return self.shipmentline_set.aggregate(
            total = Sum(F("price") * F("amount"), output_field=FloatField())
        )["total"]      

    class Meta:
        
        db_table = 'shipments'
        verbose_name = 'shipment'
        verbose_name_plural = 'shipments'
        ordering = ['id']
        
class ShipmentLine(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __star__(self):
        return f'{self.amount} of {self.product.name}'
    
    class Meta:
        
        db_table = 'shipmentLine'
        verbose_name = 'shipmentLine'
        verbose_name_plural = 'shipmentLines'
        ordering = ['id']
        
    
   