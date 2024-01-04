from django.shortcuts import render

def home(request):
    return render(request, 'f5index/index.html')

def about(request):
    return render(request, 'f5index/about.html')

def store(request):
    return render(request, 'f5index/store.html')

def services(request):
    return render(request, 'f5index/services.html')