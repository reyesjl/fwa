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
    color = models.CharField(max_length=50, default='#8b0000')
    school_image = models.ImageField(upload_to='school_images/', default='school_images/generic-school.jpg')
    rugby_image = models.ImageField(upload_to='school_images/', default='school_images/generic-rugby.jpg')
    school_level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    location = models.CharField(max_length=100)
    description = models.TextField()
    national_rank = models.IntegerField(default=0)
    student_body = models.IntegerField(default=0)
    education_description = models.TextField(default='', null=True)
    attendance_cost = models.IntegerField(default=0)
    top_programs = models.CharField(max_length=250, default='math program')
    rugby_description = models.TextField(default='', null=True)
    rugby_rank = models.IntegerField(default=0)
    rugby_coach= models.CharField(default='', max_length=50, null=True)
    rugby_video_link = models.CharField(default='',max_length=100, null=True)

    def __str__(self):
        return f"{self.name} - {self.location}"
