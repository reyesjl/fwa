from django.urls import path
from . import views

appname = 'recruiting'
urlpatterns = [
    path('', views.home, name='home'),
]