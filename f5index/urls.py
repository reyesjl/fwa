from django.urls import path
from . import views

app_name = 'f5index'
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('recruiting/', views.recruiting, name='recruiting'),
    path('tours/', views.tours, name='tours'),
    path('nutrition/', views.nutrition, name='nutrition'),
    path('training/', views.training, name='training'),
    path('club-mgmt/', views.club_mgmt, name='club-mgmt'),
    path('services/', views.services, name='services'),
]