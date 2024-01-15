# Generated by Django 5.0.1 on 2024-01-15 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruiting', '0009_school_color_school_rugby_image_school_school_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='rugby_image',
            field=models.ImageField(default='https://f5rugby.com/static/media/recruiting/generic-rugby.jpg', upload_to='school_images/'),
        ),
        migrations.AlterField(
            model_name='school',
            name='school_image',
            field=models.ImageField(default='https://f5rugby.com/static/media/recruiting/generic-school.jpg', upload_to='school_images/'),
        ),
    ]
