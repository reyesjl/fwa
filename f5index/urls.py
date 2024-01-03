from django.urls import path
from . import views

app_name = 'f5index'
urlpatterns = [
    path('', views.home, name='home'),
]