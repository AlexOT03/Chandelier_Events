# Generated by Django 4.1.9 on 2023-07-04 16:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("quote", "0002_remove_quote_service_quote_service"),
    ]

    operations = [
        migrations.AddField(
            model_name="quote",
            name="message",
            field=models.TextField(blank=True),
        ),
    ]
