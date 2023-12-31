# Generated by Django 4.1.9 on 2023-06-29 21:03

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Theme",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=40)),
                ("description", models.TextField(blank=True)),
                ("image", models.ImageField(upload_to="theme_images")),
                ("created_date", models.DateTimeField(auto_now_add=True)),
                ("is_active", models.BooleanField(default=True)),
            ],
        ),
    ]
