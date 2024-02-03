from django.db import models
from django.core.validators import MinValueValidator
from .choices import STATUS_OPTIONS, COUNTRY_OPTIONS

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
    
    