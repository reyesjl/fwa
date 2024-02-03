from django.urls import path
from . import views

app_name = 'submissions'
urlpatterns = [
    path('submission/recruiting/', views.handle_recruiting_submissions, name='recruiting_submission'),
    path('submission/tours/', views.handle_tours_submissions, name='tours_submission'),
    path('success/<str:message>/', views.success_page, name='success'),
]