from django.shortcuts import redirect, render, get_object_or_404
from django.conf import settings
from django.urls import reverse
from .models import Product
import stripe

def store(request):
    products = Product.objects.all()
    return render(request, 'product/store.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product/product_detail.html', {'product': product})

def purchase(request, product_id):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    product = get_object_or_404(Product, pk=product_id)

    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items = [{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': product.name,
                },
                'unit_amount': int(product.price * 100), # price in cents
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=request.build_absolute_uri(reverse('product:payment_success')),
        cancel_url=request.build_absolute_uri(product.get_absolute_url()),
    )

    return redirect(checkout_session.url)

def success(request):
    return render(request, 'product/success.html')
