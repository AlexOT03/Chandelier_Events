# Generated by Django 4.1.9 on 2023-07-04 19:31

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("quote", "0004_remove_quote_service_quote_service_detail"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="quote",
            name="location",
        ),
    ]
