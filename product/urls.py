from django.urls import path
from . import views

app_name = 'product'
urlpatterns = [
    path('store/products/', views.store, name='store'),
    path('store/products/<int:product_id>', views.product_detail, name='product_detail'),
    path('store/purchase/<int:product_id>', views.purchase, name='purchase'),
    path('store/purchase/success', views.success, name='payment_success'),
]