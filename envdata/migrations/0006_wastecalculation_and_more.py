# Generated by Django 5.0.1 on 2024-01-17 17:38

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('envdata', '0005_distancecalculation'),
    ]

    operations = [
        migrations.CreateModel(
            name='WasteCalculation',
            fields=[
                ('waste_name', models.CharField(max_length=255)),
                ('quantity_recycled', models.FloatField()),
                ('quantity_disposed', models.FloatField()),
                ('quantity_land_filled', models.FloatField()),
                ('created', models.DateField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='distancecalculation',
            name='fuel_consumption',
            field=models.FloatField(default=7.5),
        ),
    ]