# Generated by Django 4.1.9 on 2023-07-09 23:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("quote_pdf", "0006_alter_quotedetail_iva"),
    ]

    operations = [
        migrations.AddField(
            model_name="quotedetail",
            name="folio",
            field=models.CharField(default="", max_length=32),
        ),
    ]
