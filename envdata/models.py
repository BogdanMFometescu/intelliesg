from django.db import models
from django.db.models import Sum
import uuid
from envdata.constants import *


# Create your models here.

class Emission(models.Model):
    emission_type = models.CharField(max_length=255, blank=False, null=False, choices=EMISSION_TYPE)
    emission_scope = models.CharField(max_length=255, blank=False, null=False, choices=EMISSION_SCOPE)
    created = models.DateField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)

    @staticmethod
    def total_co2_emissions():
        total_co2 = 0
        total_co2 += FuelEmission.objects.aggregate(Sum('co2e_for_fuel_emission'))['co2e_for_fuel_emission__sum'] or 0
        total_co2 += Sf6Emission.objects.aggregate(Sum('co2e_for_sf6_emission'))['co2e_for_sf6_emission__sum'] or 0
        total_co2 += EnergyAcquisition.objects.aggregate('co2e_for_energy_emission')[
                         'co2e_for_energy_emission__sum'] or 0
        return total_co2

    def __str__(self):
        return f'{self.emission_type}'


# SCOPE 1 emissions
class FuelEmission(models.Model):
    emission_type = models.ForeignKey(Emission, on_delete=models.CASCADE)
    fuel_type = models.CharField(max_length=255, blank=False, null=False, choices=FUEL_TYPE)
    fuel_source = models.CharField(max_length=255, blank=False, null=False)
    fuel_quantity = models.FloatField(max_length=10, blank=False, null=False, default=0.00)
    pollution_norm = models.CharField(max_length=30, blank=False, null=False, choices=POLLUTION_NORM)
    activity_type = models.CharField(max_length=255, blank=False, null=False, choices=ACTIVITY_TYPE)
    vehicle_type = models.CharField(max_length=255, blank=False, null=False, choices=VEHICLE_TYPE)
    measure_unit = models.CharField(max_length=30, blank=False, null=False, default='L')
    emission_factor = models.IntegerField(blank=False, null=False, default=0, )
    created = models.DateField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)

    @property
    def co2e_for_fuel_emission(self):
        total_co2 = self.fuel_quantity * self.emission_factor
        return total_co2

    def __str__(self):
        return f'{self.fuel_type}'


class Sf6Emission(models.Model):
    emission_type = models.ForeignKey(Emission, on_delete=models.CASCADE)
    equipment_type = models.CharField(max_length=255, blank=False, null=False)
    equipment_producer = models.CharField(max_length=255, blank=False, null=False)
    sf6_quantity = models.FloatField(max_length=10, blank=False, null=False)
    created = models.DateField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)

    @property
    def co2e_for_sf6_emission(self):
        total_co2 = self.sf6_quantity * 1
        return total_co2


class RefrigerantEmission(models.Model):
    emission_type = models.ForeignKey(Emission, on_delete=models.CASCADE)
    equipment_type = models.CharField(max_length=255, blank=False, null=False)
    refrigerant_type = models.CharField(max_length=255, blank=False, null=False)
    refrigerant_quantity = models.FloatField(max_length=10, blank=False, null=False, default=0.00)
    created = models.DateField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)

    def __str__(self):
        return f'{self.refrigerant_type}'


# SCOPE 2 emissions


class EnergyAcquisition(models.Model):
    emission_type = models.ForeignKey(Emission, on_delete=models.CASCADE)
    location = models.CharField(max_length=255, blank=False, null=False)
    supplier_name = models.CharField(max_length=255, blank=False, null=False)
    measure_unit = models.CharField(max_length=20, blank=False, null=False)
    emission_factor = models.IntegerField(blank=False, null=True, default=0, )
    calculation_method = models.CharField(max_length=255, blank=False, null=False)
    created = models.DateField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)

    @property
    def co2e_for_energy_emission(self):
        total_co2 = self.emission_factor * 1
        return total_co2

    def __str__(self):
        return f'{self.supplier_name}'


class DistanceCalculation(models.Model):
    origin = models.CharField(max_length=255, blank=False, null=False)
    destination = models.CharField(max_length=255, blank=False, null=False)
    distance = models.FloatField(blank=False, null=False)
    created = models.DateField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)

    def __str__(self):
        return f'{self.distance}'
