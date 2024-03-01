from django.urls import path
from . import views

app_name = 'store'
urlpatterns = [
    path('store/', views.store, name='store'),
    path('store/category/<str:category_name>/', views.products_by_category, name='products_by_category'),
    path('store/products/', views.products, name='products'),
    path('store/products/<int:product_id>/', views.product_details, name='product_details'),
    path('store/products/purchase/<int:product_id>/', views.purchase, name='purchase'),
    path('store/products/purchase/success/', views.success, name='payment_success'),
    path('store/products/purchase/webhook_success/', views.stripe_webhook_payment_success, name='webhook_payment_success'),
]