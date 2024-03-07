from django.shortcuts import render
from plans.models import PlayerPlan

def home(request):
    return render(request, 'f5index/index.html')

def about(request):
    return render(request, 'f5index/about.html')

def store(request):
    return render(request, 'f5index/store.html')

def recruiting(request):
    return render(request, 'f5index/recruiting.html')

def tours(request):
    return render(request, 'f5index/tours.html')

def nutrition(request):
    return render(request, 'f5index/nutrition.html')

def training(request):
    return render(request, 'f5index/training.html')

def club_mgmt(request):
    return render(request, 'f5index/club_mgmt.html')

def services(request):
    plans = PlayerPlan.objects.all()
    
    context = {
        'plans': plans,
    }
    return render(request, 'f5index/services.html', context)