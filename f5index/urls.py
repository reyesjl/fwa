from django.urls import path
from . import views

app_name = 'f5index'
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('store/', views.store, name='store'),
    path('recruiting/', views.recruiting, name='recruiting'),
    path('tours/', views.tours, name='tours'),
    path('services/', views.services, name='services'),
]