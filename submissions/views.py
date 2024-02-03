from django.shortcuts import redirect, render
from .forms import RecruitingSubmissionForm

def handle_recruiting_submissions(request):
    title = 'Apply to Study Abroad'
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
    return render(request, 'submissions/handle_submission_form.html', context)
        
def success_page(request, message):
    return render(request, 'submissions/success.html', {'message' : message})