from django.db import models
from django.core.validators import MinValueValidator

class PlayerEntry(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Reviewed', 'Reviewed'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    ]

    name = models.CharField(max_length=100)
    age = models.IntegerField(validators=[MinValueValidator(14)])
    school_of_interest = models.CharField(max_length=100)
    rugby_history = models.TextField()
    cover_letter = models.TextField()
    country_of_residence = models.CharField(max_length=100)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=15)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"{self.name} - {self.country_of_residence}"
    
class School(models.Model):
    LEVEL_CHOICES = [
        ('HS', 'High School'),
        ('CO', 'College'),
    ]

    name = models.CharField(max_length=100)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    location = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.location}"
