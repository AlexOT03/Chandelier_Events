# Generated by Django 4.1.9 on 2023-07-09 03:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("quote_pdf", "0004_quotedetail_update_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="quotedetail",
            name="discount",
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name="quotedetail",
            name="iva",
            field=models.IntegerField(choices=[(0, 0), (1, 5), (2, 10), (3, 15)]),
        ),
        migrations.AlterField(
            model_name="quotedetail",
            name="transport",
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=8, null=True),
        ),
    ]
