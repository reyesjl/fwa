from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.urls import reverse
from .models import Product, ProductVariant
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

def store(request):
    products = Product.objects.filter(is_available=True)
    return render(request, 'store/store.html', {'products': products})

def products(request):
    products = Product.objects.filter(is_available=True)
    return render(request, 'store/products.html', {'products': products})

def product_details(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'store/product_details.html', {'product': product})

def purchase(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': product.title,
                },
                'unit_amount': int(product.price * 100),  # price in cents
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=request.build_absolute_uri(reverse('success')),
        cancel_url=request.build_absolute_uri(product.get_absolute_url()),
        metadata={
            'product_id': str(product.id),  # Include product ID
            'product_title': product.title,  # Include product title
        },
    )

    return redirect(checkout_session.url)

def success(request):
    return render(request, 'store/success.html')

@csrf_exempt
def stripe_webhook_payment_success(request):
    payload = request.body
    sig_header = request.headers.get('Stripe-Signature')

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_SUCCESS_WEBHOOK_PRIVATE
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        handle_payment_success(session)

    return HttpResponse(status=200)

def handle_payment_success(session):
    product_id = session['metadata'].get('product_id')
    if product_id:
        product = Product.objects.get(id=product_id)
        product.stock_quantity -= 1  # Assuming one item is purchased per transaction
        product.save()