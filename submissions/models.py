from django.db import models
from django.core.validators import MinValueValidator
from .choices import STATUS_OPTIONS, COUNTRY_OPTIONS, TEAM_ITEM_OPTIONS

class BaseSubmissionModel(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.CharField(max_length=150)
    phone = models.CharField(max_length=150)
    status = models.CharField(choices=STATUS_OPTIONS, max_length=20, default='Unseen')

    class Meta:
        abstract = True

class RecruitingSubmission(BaseSubmissionModel):
    position = models.CharField(max_length=50, default='prop')
    age = models.IntegerField(default="12", validators=[MinValueValidator(12),])
    origin_country = models.CharField(max_length=50, default='usa')
    destination_country = models.CharField(choices=COUNTRY_OPTIONS, max_length=50, default='United States')

class ToursSubmission(BaseSubmissionModel):
    teamname = models.CharField(max_length=100, default='Firstfive RFC')
    teamsize = models.IntegerField(default="15", validators=[MinValueValidator(15),])

class CanterburyKitSubmission(BaseSubmissionModel):
    teamname = models.CharField(max_length=100, default='Firstfive RFC')
    teamsize = models.IntegerField(default="15", validators=[MinValueValidator(15),])

class TeamItemSubmission(BaseSubmissionModel):
    product_name = models.CharField(choices=TEAM_ITEM_OPTIONS, max_length=50, default='Rugby Caps')
    teamname = models.CharField(max_length=100, default='Firstfive RFC')
    team_primary_color = models.CharField(max_length=50, default='red')
    team_secondary_color = models.CharField(max_length=50, default='black')
    teamsize = models.IntegerField(default="15", validators=[MinValueValidator(15),])

class Issue(models.Model):
    email = models.EmailField()
    problem_description = models.TextField()
    status = models.CharField(choices=STATUS_OPTIONS, max_length=20, default='Unseen')

    def __str__(self):
        return f"Issue reported by {self.email}"
    
class Feedback(models.Model):
    email = models.EmailField()
    feedback = models.TextField()
    status = models.CharField(choices=STATUS_OPTIONS, max_length=20, default='Unseen')

    def __str__(self):
        return f"Feedback submitted by {self.email}"
    
class Design(models.Model):
    email = models.EmailField()
    design_description = models.TextField()
    status = models.CharField(choices=STATUS_OPTIONS, max_length=20, default='Unseen')

    def __str__(self):
        return f"Design submitted by {self.email}"

class Specialist(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField()
    cell = models.CharField(max_length=15)
    help_details = models.TextField()
    status = models.CharField(choices=STATUS_OPTIONS, max_length=20, default='Unseen')

    def __str__(self):
        return f"Specialist request submitted by {self.email}"