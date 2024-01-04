from django.shortcuts import render

def home(request):
    return render(request, 'f5index/index.html')