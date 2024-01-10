from django.urls import path
from . import views

app_name = 'product'
urlpatterns = [
    path('store/products/', views.store, name='store'),
    path('store/products/<int:product_id>', views.product_detail, name='product_detail'),
]