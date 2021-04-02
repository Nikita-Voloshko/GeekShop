from django.contrib import admin
from mineapp.models import products, ProductCategory

# Register your models here.

admin.site.register(products)
admin.site.register(ProductCategory)

