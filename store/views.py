from django.shortcuts import render

def store(request):
    return render(request, 'store/store.html', {'item_count':5,})