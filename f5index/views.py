from django.shortcuts import render
from product.models import Product

def home(request):
    products = Product.objects.all()
    return render(request, 'f5index/index.html', {'products': products})

def about(request):
    return render(request, 'f5index/about.html')

def store(request):
    return render(request, 'f5index/store.html')

def recruiting(request):
    return render(request, 'f5index/recruiting.html')

def tours(request):
    return render(request, 'f5index/tours.html')

def services(request):
    return render(request, 'f5index/services.html')