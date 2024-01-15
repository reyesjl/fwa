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
    school_level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    location = models.CharField(max_length=100)
    description = models.TextField()
    national_rank = models.IntegerField(default=0)
    student_body = models.IntegerField(default=0)
    education_description = models.TextField(default='')
    attendance_cost = models.IntegerField(default=0)
    top_programs = models.CharField(max_length=250, default='math program')
    rugby_description = models.TextField(default='')
    rugby_rank = models.IntegerField(default=0)
    rugby_coach= models.CharField(default='', max_length=50)
    rugby_video_link = models.CharField(default='',max_length=100)

    def __str__(self):
        return f"{self.name} - {self.location}"
