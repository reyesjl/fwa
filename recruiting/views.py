from django.shortcuts import render, redirect
from .models import School
from .forms import PlayerEntryForm

def home(request):
    schools = School.objects.all()
    return render(request,'recruiting/home.html', {'schools': schools})

def player_entry_view(request):
    if request.method == 'POST':
        form = PlayerEntryForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect the user to the success page
            return redirect('recruiting:apply_success')
    else:
        form = PlayerEntryForm()
    
    return render(request, 'recruiting/player_entry_view.html', {'form': form})

def success(request):
    return render(request, 'recruiting/success.html')