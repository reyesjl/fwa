from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.urls import reverse
from .models import Product, ProductVariant
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

def store(request):
    # Fetch products for each category
    featured_products = Product.objects.filter(category='Featured', is_available=True).prefetch_related('variants', 'images')
    vintage_products = Product.objects.filter(category='Vintage', is_available=True).prefetch_related('variants', 'images')
    signed_products = Product.objects.filter(category='Signed', is_available=True).prefetch_related('variants', 'images')
    team_products = Product.objects.filter(category='Team', is_available=True).prefetch_related('variants', 'images')
    donation_products = Product.objects.filter(category='Donation', is_available=True).prefetch_related('variants', 'images')

    # Optionally, you can fetch the first variant and main image for each product
    for products in [vintage_products, signed_products, team_products, donation_products]:
        for product in products:
            product.first_variant = product.variants.first()
            product.main_image = product.images.filter(is_main=True).first()
    context = {
        'featured_products': featured_products,
        'vintage_products': vintage_products,
        'signed_products': signed_products,
        'team_products': team_products,
        'donation_products': donation_products
        }
    return render(request, 'store/store.html', context)

def products(request):
    products = Product.objects.filter(is_available=True)
    return render(request, 'store/products.html', {'products': products})

def product_details(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product_with_prefetched_data = Product.objects.prefetch_related('variants', 'images').get(id=product_id)
    variants = product_with_prefetched_data.variants.filter(stock_quantity__gt=0).order_by('-size')
    images = product_with_prefetched_data.images.all()

    # Initialize a dictionary to store variant existence
    variant_exists = {size: False for size in ['Small', 'Medium', 'Large']}

    # Iterate over the variants and update existence dictionary
    for variant in variants:
        variant_exists[variant.size] = True
    
    # Check if this is a team item
    team_item = False
    if product.category == "Team":
        team_item = True

    
    context = {
        "product": product, 
        "variants": variants, 
        "images": images,
        "team_item": team_item,
        "variant_exists": variant_exists,
    }
    return render(request, 'store/product_details.html', context)

def purchase(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    # Get the selected variant (assuming the user has selected a variant)
    selected_variant = product.variants.first()  # Update this to fetch the selected variant

    # Ensure a variant is selected before proceeding
    if selected_variant is None:
        # Handle case where no variant is selected
        return HttpResponse("No variant selected.")

    # Prepare line item for Stripe checkout session
    line_item = {
        "price_data": {
            "currency": "usd",
            "product_data": {
                "name": product.title,
            },
            "unit_amount": int(selected_variant.price * 100),  # Convert price to cents
        },
        "quantity": 1,
    }

    # Create Stripe checkout session
    checkout_session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[line_item],
        mode="payment",
        success_url=request.build_absolute_uri(reverse('store:payment_success')),
        cancel_url=request.build_absolute_uri(reverse('store:product_details', args=[product.id])),
        metadata={
            "product_id": str(product.id),  # Include product ID
            "product_title": product.title,  # Include product title
            "variant_id": str(selected_variant.id),  # Include variant ID
            "variant_size": selected_variant.size,  # Include variant size
        },
        payment_intent_data={
            "metadata": {
                "product_id": str(product.id),  # Include product ID
                "product_title": product.title,  # Include product title
                "variant_id": str(selected_variant.id),  # Include variant ID
                "variant_size": selected_variant.size,  # Include variant size
            }
        }
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
    metadata = session.get('metadata', {})
    product_id = metadata.get('product_id')
    variant_id = metadata.get('variant_id')
    quantity = 1

    if product_id and variant_id:
        product_variant = ProductVariant.objects.get(id=variant_id)
        product_variant.stock_quantity -= quantity
        product_variant.save()