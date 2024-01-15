# Generated by Django 5.0.1 on 2024-01-15 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruiting', '0005_remove_playerentry_country_of_interest'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='attendance_cost',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='school',
            name='education_description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='school',
            name='national_rank',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='school',
            name='rugby_coach',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='school',
            name='rugby_description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='school',
            name='rugby_rank',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='school',
            name='rugby_video_link',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='school',
            name='student_body',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='school',
            name='top_programs',
            field=models.CharField(default='math program', max_length=250),
        ),
    ]
