# Generated by Django 5.0.1 on 2024-04-01 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('envdata', '0002_alter_energy_emission_type_alter_fuel_emission_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='target',
            name='intermediate_year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]