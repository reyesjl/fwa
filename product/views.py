from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.urls import reverse
from .models import Product
import stripe

def store(request):
    products = Product.objects.filter(active=True)
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
        metadata={
            'product_id': str(product.id),# Convert to string
        },
    )

    return redirect(checkout_session.url)

def success(request):
    return render(request, 'product/success.html')

@csrf_exempt
def payment_success_webhook(request):
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
        product.stock -= 1  # Assuming one item is purchased per transaction
        product.save()