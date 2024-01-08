# Generated by Django 5.0.1 on 2024-01-08 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruiting', '0002_playerentry_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('school_level', models.CharField(choices=[('HS', 'High School'), ('CO', 'College')], max_length=20)),
                ('location', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
    ]
