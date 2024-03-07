from django.db import models

class PlayerPlan(models.Model):
    PLAN_CATEGORIES = (
        ('Strength', 'Strength'),
        ('Mobility', 'Mobility'),
        ('Speed', 'Speed'),
        ('Power', 'Power'),
        ('Cardio', 'Cardio'),
        ('Nutrition', 'Nutrition'),
    )
    
    plan_name = models.CharField(max_length=100)
    plan_category = models.CharField(max_length=50, choices=PLAN_CATEGORIES)
    plan_file = models.FileField(upload_to='player_plans/')
    plan_picture = models.ImageField(upload_to='plan_images/', null=True, blank=True)
    
    def __str__(self):
        return self.plan_name