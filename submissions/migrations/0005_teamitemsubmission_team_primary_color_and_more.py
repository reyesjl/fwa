# Generated by Django 5.0.1 on 2024-02-14 18:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("submissions", "0004_teamitemsubmission"),
    ]

    operations = [
        migrations.AddField(
            model_name="teamitemsubmission",
            name="team_primary_color",
            field=models.CharField(default="red", max_length=50),
        ),
        migrations.AddField(
            model_name="teamitemsubmission",
            name="team_secondary_color",
            field=models.CharField(default="black", max_length=50),
        ),
        migrations.AlterField(
            model_name="teamitemsubmission",
            name="product_name",
            field=models.CharField(
                choices=[("Rugby Caps", "Rugby Caps")],
                default="Rugby Caps",
                max_length=50,
            ),
        ),
    ]