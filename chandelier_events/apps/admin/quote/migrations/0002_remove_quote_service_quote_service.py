# Generated by Django 4.1.9 on 2023-07-03 20:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("service", "0001_initial"),
        ("quote", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="quote",
            name="service",
        ),
        migrations.AddField(
            model_name="quote",
            name="service",
            field=models.ManyToManyField(to="service.service"),
        ),
    ]
