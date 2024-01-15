from django.shortcuts import render, redirect, get_object_or_404
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

def school_detail(request, school_id):
    school = get_object_or_404(School, pk=school_id)

    # Split comma-separated values into a list
    top_programs = school.top_programs.split(',')
    return render(request, 'recruiting/school_detail.html', {'school':school, 'top_programs':top_programs})

def success(request):
    return render(request, 'recruiting/success.html')