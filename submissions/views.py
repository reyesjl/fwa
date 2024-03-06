"""
Submissions Views
=================

This module contains view functions for handling various types of form submissions, including recruiting interest, tours interest, team item interest, issue reporting, feedback submission, design submission, and specialist help request.

Functions:
- handle_recruiting_submissions(request): Handles the submission of the study abroad interest form.
- handle_tours_submissions(request): Handles the submission of the tours interest form.
- handle_team_item_submissions(request): Handles the submission of the team item interest form.
- handle_issue_submission(request): Handles the submission of the issue reporting form.
- handle_feedback_submission(request): Handles the submission of the feedback form.
- handle_design_submission(request): Handles the submission of the design submission form.
- handle_specialist_submission(request): Handles the submission of the specialist help request form.
- success_page(request, message): Renders the success page with a success message.

"""

from django.shortcuts import redirect, render
from .forms import (
    RecruitingSubmissionForm, 
    ToursSubmissionForm, 
    TeamItemSubmissionForm, 
    IssueForm, 
    FeedbackForm, 
    DesignForm, 
    SpecialistForm
)

def handle_recruiting_submissions(request):
    """
    Renders the study abroad interest form and handles its submission.
    
    If the form is submitted via POST request and is valid, saves the form data and redirects to the success page.
    Otherwise, re-renders the form with validation errors.
    """
    title = 'Study Abroad Interest Form'
    form = RecruitingSubmissionForm()
    if request.method == 'POST':
        form = RecruitingSubmissionForm(request.POST)
        if form.is_valid():
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
    """
    Renders the tours interest form and handles its submission.
    
    If the form is submitted via POST request and is valid, saves the form data and redirects to the success page.
    Otherwise, re-renders the form with validation errors.
    """
    title = 'Tours Interest Form'
    form = ToursSubmissionForm()
    if request.method == 'POST':
        form = ToursSubmissionForm(request.POST)
        if form.is_valid():
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
    """
    Renders the team item interest form and handles its submission.
    
    If the form is submitted via POST request and is valid, saves the form data and redirects to the success page.
    Otherwise, re-renders the form with validation errors.
    """
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
    """
    Renders the issue reporting form and handles its submission.
    
    If the form is submitted via POST request and is valid, saves the form data and redirects to the success page.
    Otherwise, re-renders the form with validation errors.
    """
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


def handle_feedback_submission(request):
    """
    Renders the feedback form and handles its submission.
    
    If the form is submitted via POST request and is valid, saves the form data and redirects to the success page.
    Otherwise, re-renders the form with validation errors.
    """
    title = 'Submit Feedback'
    form = FeedbackForm()

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('submissions:success', message='Your feedback has been successfully submitted')
        else:
            # Re-render the form with validation errors
            form = FeedbackForm(request.POST)

    context = {
        'form': form,
        'title': title,
    }
    return render(request, 'submissions/handle_feedback_form.html', context)


def handle_design_submission(request):
    """
    Renders the design submission form and handles its submission.
    
    If the form is submitted via POST request and is valid, saves the form data and redirects to the success page.
    Otherwise, re-renders the form with validation errors.
    """
    title = 'Submit Design'
    form = DesignForm()

    if request.method == 'POST':
        form = DesignForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('submissions:success', message='Your design has been successfully submitted')
        else:
            # Re-render the form with validation errors
            form = DesignForm(request.POST)

    context = {
        'form': form,
        'title': title,
    }
    return render(request, 'submissions/handle_design_form.html', context)


def handle_specialist_submission(request):
    """
    Renders the specialist help request form and handles its submission.
    
    If the form is submitted via POST request and is valid, saves the form data and redirects to the success page.
    Otherwise, re-renders the form with validation errors.
    """
    title = 'Request Specialist Help'
    form = SpecialistForm()

    if request.method == 'POST':
        form = SpecialistForm(request.POST)
        if form.is_valid():
            form.save()
            message = "Your request for a specialist has been submitted. A member of our team will be in contact with you soon. Be sure to check your spam folder."
            return redirect('submissions:success', message=message)
        else:
            # Re-render the form with validation errors
            form = SpecialistForm(request.POST)

    context = {
        'form': form,
        'title': title,
    }
    return render(request, 'submissions/handle_specialist_form.html', context)


def success_page(request, message):
    """
    Renders the success page with a success message.
    """
    return render(request, 'submissions/success.html', {'message' : message})