# Generated by Django 4.1.9 on 2023-07-09 03:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("theme", "0001_initial"),
        ("quote", "0008_remove_quote_budget"),
    ]

    operations = [
        migrations.AlterField(
            model_name="quote",
            name="theme",
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to="theme.theme"
            ),
        ),
    ]
