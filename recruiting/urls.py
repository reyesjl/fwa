from django.urls import path
from . import views

app_name = 'recruiting'
urlpatterns = [
    path('services/recruiting/', views.home, name='home'),
    path('services/recruiting/apply', views.player_entry_view, name='apply'),
    path('services/recruiting/success', views.success, name='apply_success'),
    path('services/recruiting/schools/<int:school_id>', views.school_detail, name='school_detail'),
]