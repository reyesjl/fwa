from django.db import models
from django.core.validators import MinValueValidator

class PlayerEntry(models.Model):
    COUNTRY_CHOICES = [
        ('USA', 'United States of America'),
        ('IRE', 'Ireland'),
        ('SCT', 'Scotland'),
        ('ENG', 'England'),
        # Add more country choices as needed
    ]

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Reviewed', 'Reviewed'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    ]

    name = models.CharField(max_length=100)
    age = models.IntegerField(validators=[MinValueValidator(14)])
    country_of_interest = models.CharField(max_length=3, choices=COUNTRY_CHOICES)
    school_of_interest = models.CharField(max_length=100)
    rugby_history = models.TextField()
    cover_letter = models.TextField()
    country_of_residence = models.CharField(max_length=100)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=15)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"{self.name} - {self.country_of_residence}"
