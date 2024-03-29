from datetime import datetime, timedelta
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.urls import reverse
from .models import Product, ProductVariant, ProductImage
from django.db.models import Subquery, OuterRef
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

def store(request):
    # Set date range
    one_month_ago = datetime.now() - timedelta(days=30)

    # Fetch latest products within date range
    latest_products = Product.objects.all().filter(created_at__gte=one_month_ago)

    context = {'latest_products': latest_products}
    return render(request, 'store/store.html', context)

def products_by_category(request):
    category_name = request.GET.get('category_name')
    category_products = Product.objects.get_products_by_category(category_name)

    context = {'category_name': category_name, 'category_products': category_products}
    return render(request, 'store/products_by_category.html', context)

def product_details(request, product_id):
    product = get_object_or_404(Product.objects.with_first_variant_and_main_image(), id=product_id)
    variants = product.variants.all()
    images = product.images.all()
    unique_colors = set(variant.color for variant in variants)
    team_item = product.is_team_item()

    context = {
        "product": product, 
        "variants": variants, 
        "images": images,
        "team_item": team_item,
        "unique_colors": unique_colors,
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