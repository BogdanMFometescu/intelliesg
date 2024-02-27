from django.db import models
from django.db.models import Sum
import uuid
from envdata.constants import *


class Company(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=False, null=False)
    address = models.CharField(max_length=255, blank=False, null=False)
    city = models.CharField(max_length=255, blank=False, null=False)
    country = models.CharField(max_length=255, blank=False, null=False)
    phone = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(max_length=255, blank=False, null=False)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    @property
    def total_co2_emissions(self):
        total_co2 = 0
        total_co2 += Fuel.objects.aggregate(Sum('co2e_for_fuel_emission'))['co2e_for_fuel_emission__sum'] or 0
        total_co2 += Sf6.objects.aggregate(Sum('co2e_for_sf6_emission'))['co2e_for_sf6_emission__sum'] or 0
        total_co2 += Energy.objects.aggregate('co2e_for_energy_emission')[
                         'co2e_for_energy_emission__sum'] or 0
        return total_co2

    def __str__(self):
        return self.name


# SCOPE 1 emissions
class Fuel(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    emission_type = models.CharField(max_length=255, blank=False, null=False, choices=EMISSION_TYPE)
    emission_scope = models.CharField(max_length=255, blank=False, null=False, choices=EMISSION_SCOPE)
    fuel_type = models.CharField(max_length=255, blank=False, null=False, choices=FUEL_TYPE)
    fuel_source = models.CharField(max_length=255, blank=False, null=False)
    fuel_quantity = models.FloatField(max_length=10, blank=False, null=False, default=0.00)
    pollution_norm = models.CharField(max_length=30, blank=False, null=False, choices=POLLUTION_NORM)
    activity_type = models.CharField(max_length=255, blank=False, null=False, choices=ACTIVITY_TYPE)
    vehicle_type = models.CharField(max_length=255, blank=False, null=False, choices=VEHICLE_TYPE)
    measure_unit = models.CharField(max_length=30, blank=False, null=False, default='L')
    emission_factor = models.IntegerField(blank=False, null=False, default=0, )
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)

    @property
    def co2e_for_fuel_emission(self):
        total_co2 = self.fuel_quantity * self.emission_factor
        return total_co2

    def __str__(self):
        return f'{self.fuel_type}'


class Sf6(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    emission_type = models.CharField(max_length=255, blank=False, null=False, choices=EMISSION_TYPE)
    emission_scope = models.CharField(max_length=255, blank=False, null=False, choices=EMISSION_SCOPE)
    equipment_type = models.CharField(max_length=255, blank=False, null=False)
    equipment_producer = models.CharField(max_length=255, blank=False, null=False)
    sf6_quantity = models.FloatField(max_length=10, blank=False, null=False)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)

    @property
    def co2e_for_sf6_emission(self):
        total_co2 = self.sf6_quantity * 1
        return total_co2


class Refrigerant(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    emission_type = models.CharField(max_length=255, blank=False, null=False, choices=EMISSION_TYPE)
    emission_scope = models.CharField(max_length=255, blank=False, null=False, choices=EMISSION_SCOPE)
    refrigerant_type = models.CharField(max_length=255, blank=False, null=False)
    refrigerant_quantity = models.FloatField(max_length=10, blank=False, null=False, default=0.00)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)

    def __str__(self):
        return f'{self.refrigerant_type}'


# SCOPE 2 emissions


class Energy(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    emission_type = models.CharField(max_length=255, blank=False, null=False, choices=EMISSION_TYPE)
    emission_scope = models.CharField(max_length=255, blank=False, null=False, choices=EMISSION_SCOPE)
    location = models.CharField(max_length=255, blank=False, null=False)
    supplier_name = models.CharField(max_length=255, blank=False, null=False)
    measure_unit = models.CharField(max_length=20, blank=False, null=False)
    emission_factor = models.IntegerField(blank=False, null=True, default=0, )
    calculation_method = models.CharField(max_length=255, blank=False, null=False)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)

    @property
    def co2e_for_energy_emission(self):
        total_co2 = self.emission_factor * 1
        return total_co2

    def __str__(self):
        return f'{self.supplier_name}'


class Travel(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    emission_type = models.CharField(max_length=255, blank=False, null=False, choices=EMISSION_TYPE)
    emission_scope = models.CharField(max_length=255, blank=False, null=False, choices=EMISSION_SCOPE)
    origin = models.CharField(max_length=255, blank=False, null=False)
    destination = models.CharField(max_length=255, blank=False, null=False)
    distance = models.FloatField(blank=False, null=False)
    fuel_consumption = models.FloatField(blank=False, null=False, default=7.5)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)

    @property
    def co2_for_distance_calculation(self):
        total_co2 = ((self.distance * self.fuel_consumption) / 100) * 10.8
        return total_co2

    def __str__(self):
        return f'{self.distance}'


class Waste(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    emission_type = models.CharField(max_length=255, blank=False, null=False, choices=EMISSION_TYPE)
    emission_scope = models.CharField(max_length=255, blank=False, null=False, choices=EMISSION_SCOPE)
    waste_name = models.CharField(max_length=255, blank=False, null=False)
    quantity_recycled = models.FloatField(blank=False, null=False)
    quantity_disposed = models.FloatField(blank=False, null=False)
    quantity_land_filled = models.FloatField(blank=False, null=False)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, unique=True)

    def __str__(self):
        return f'{self.waste_name}'

    @property
    def total_waste_quantity(self):
        total_quantity = self.quantity_disposed + self.quantity_recycled + self.quantity_land_filled
        return total_quantity

    @property
    def c02_for_waste_quantity(self):
        total_co2 = self.total_waste_quantity * 1  # TODO search for the right formula
        return total_co2
