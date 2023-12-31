from django.contrib import admin
from .models import ProdCategory, Product

class ProdCategoryAdmin(admin.ModelAdmin):
    
    readonly_fields = ('created', 'updated')
    
class ProductAdmin(admin.ModelAdmin):
    
    readonly_fields = ('created', 'updated')
    
admin.site.register(ProdCategory, ProdCategoryAdmin)
admin.site.register(Product, ProductAdmin)

