# Generated by Django 5.0.1 on 2024-12-11 20:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("envdata", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="fuel",
            name="fuel_quantity",
        ),
    ]
