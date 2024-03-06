from django.shortcuts import redirect, render
from .forms import RecruitingSubmissionForm, ToursSubmissionForm, TeamItemSubmissionForm, IssueForm

def handle_recruiting_submissions(request):
    title = 'Study Abroad Interest Form'
    form = RecruitingSubmissionForm()
    if request.method == 'POST':
        form = RecruitingSubmissionForm(request.POST)
        if form.is_valid():
            # process any data from the form here
            form.save()
            return redirect('submissions:success', message='Your recruiting submission was successful')
        else:
            form = RecruitingSubmissionForm()

    context = {
        'form': form,
        'title': title,
    }
    return render(request, 'submissions/handle_recruiting_form.html', context)

def handle_tours_submissions(request):
    title = 'Tours Interest Form'
    form = ToursSubmissionForm()
    if request.method == 'POST':
        form = ToursSubmissionForm(request.POST)
        if form.is_valid():
            # process any data from the form here
            form.save()
            return redirect('submissions:success', message='Your tours quote form has been submitted')
        else:
            form = ToursSubmissionForm()

    context = {
        'form': form,
        'title': title,
    }
    return render(request, 'submissions/handle_tours_form.html', context)

def handle_team_item_submissions(request):
    title = 'Team Item Interest Form'
    form = TeamItemSubmissionForm()

    if request.method == 'POST':
        form = TeamItemSubmissionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('submissions:success', message='Your team item form has been submitted')
        else:
            form = TeamItemSubmissionForm()  # Ensure form remains read-only

    context = {
        "form": form,
        "title": title,
    }
    return render(request, 'submissions/handle_team_item_form.html', context)

def handle_issue_submission(request):
    title = 'Report an Issue'
    form = IssueForm()

    if request.method == 'POST':
        form = IssueForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('submissions:success', message='Your issue has been successfully reported')
        else:
            # Re-render the form with validation errors
            form = IssueForm(request.POST)

    context = {
        'form': form,
        'title': title,
    }
    return render(request, 'submissions/handle_issue_form.html', context)
        
def success_page(request, message):
    return render(request, 'submissions/success.html', {'message' : message})