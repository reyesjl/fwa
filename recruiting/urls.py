from django.urls import path
from . import views

app_name = 'recruiting'
urlpatterns = [
    path('services/recruiting/', views.home, name='home'),
]