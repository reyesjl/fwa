from django.contrib import admin
from .models import Product, ProductDetail, ProductImage

admin.site.register(Product)
admin.site.register(ProductDetail)
admin.site.register(ProductImage)

