from django.shortcuts import render, get_object_or_404
from .models import Product

def store(request):
    products = Product.objects.all()
    return render(request, 'product/store.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product/product_detail.html', {'product': product})
