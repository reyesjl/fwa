from django.urls import path
from . import views

app_name = 'product'
urlpatterns = [
    path('store/', views.store, name='store'),
]