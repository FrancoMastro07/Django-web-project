from django.db import models

class ProdCategory(models.Model):
    
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        
        verbose_name = "ProdCategory"
        verbose_name_plural = "ProdsCategory"
        
    def __str__(self):
        
        return self.name
    
class Product(models.Model):
    
    name = models.CharField(max_length=50)
    categories = models.ForeignKey(ProdCategory, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="store", null=True, blank=True)
    price = models.FloatField()
    availability = models.BooleanField()
