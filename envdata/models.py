from django.db import models
from django.db.models import Sum, F
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
        fuel_co2e = Fuel.fuel_co2e_per_company(self.id)
        refrigerant_co2e = Refrigerant.refrigerant_co2e_per_company(self.id)
        sf6_co2e = Sf6.sf6_co2e_per_company(self.id)
        travel_co2e = Travel.travel_co2e_per_company(self.id)
        energy_co2e = Energy.energy_co2e_per_company(self.id)
        waste_co2e = Waste.waste_co2e_per_company(self.id)

        total_co2e = sum([fuel_co2e, refrigerant_co2e, sf6_co2e, travel_co2e, energy_co2e, waste_co2e])
        return total_co2e

    @property
    def fuel_co2e(self):
        return Fuel.fuel_co2e_per_company(self.id)

    @property
    def refrigerant_co2e(self):
        return Refrigerant.refrigerant_co2e_per_company(self.id)

    @property
    def sf6_co2e(self):
        return Sf6.sf6_co2e_per_company(self.id)

    @property
    def travel_co2e(self):
        return Travel.travel_co2e_per_company(self.id)

    @property
    def energy_co2e(self):
        return Energy.energy_co2e_per_company(self.id)

    @property
    def waste_co2e(self):
        return Waste.waste_co2e_per_company(self.id)

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

    @classmethod
    def fuel_co2e_per_company(cls, company_id):
        fuel_co2e_per_company = \
            cls.objects.filter(company_id=company_id).aggregate(
                total_co2=Sum(F('fuel_quantity') * F('emission_factor')))[
                'total_co2'] or 0
        return fuel_co2e_per_company

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

    @classmethod
    def sf6_co2e_per_company(cls, company_id):
        sf6_co2e_per_company = cls.objects.filter(company=company_id).aggregate(total_co2=Sum('sf6_quantity'))[
                                   'total_co2'] or 0
        return sf6_co2e_per_company


class Refrigerant(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    emission_type = models.CharField(max_length=255, blank=False, null=False, choices=EMISSION_TYPE)
    emission_scope = models.CharField(max_length=255, blank=False, null=False, choices=EMISSION_SCOPE)
    refrigerant_type = models.CharField(max_length=255, blank=False, null=False)
    refrigerant_quantity = models.FloatField(max_length=10, blank=False, null=False, default=0.00)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)

    @property
    def co2e_for_refrigerant(self):
        total_co2 = self.refrigerant_quantity * 1
        return total_co2

    @classmethod
    def refrigerant_co2e_per_company(cls, company_id):
        refrigerant_co2e_per_company = \
            cls.objects.filter(company=company_id).aggregate(total_co2=Sum('refrigerant_quantity'))[
                'total_co2'] or 0
        return refrigerant_co2e_per_company

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
    energy_quantity = models.FloatField(max_length=20, blank=False, null=False, default=0.00)
    emission_factor = models.IntegerField(blank=False, null=True, default=0, )
    calculation_method = models.CharField(max_length=255, blank=False, null=False)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)

    @property
    def co2e_for_energy_emission(self):
        total_co2 = self.emission_factor * self.energy_quantity
        return total_co2

    @classmethod
    def energy_co2e_per_company(cls, company_id):
        energy_co2e_per_company = \
            cls.objects.filter(company_id=company_id).aggregate(
                total_co2=Sum(F('energy_quantity') * F('emission_factor')))[
                'total_co2'] or 0
        return energy_co2e_per_company

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

    @classmethod
    def travel_co2e_per_company(cls, company_id):
        travel_co2_per_company = cls.objects.filter(company_id=company_id).aggregate(
            total_co2=Sum((F('fuel_consumption') * F('distance')) / 100) * 10.8)[
                                     'total_co2'] or 0
        return travel_co2_per_company

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

    @property
    def total_waste_quantity(self):
        total_co2 = (self.quantity_disposed + self.quantity_land_filled - self.quantity_recycled) * 1
        return total_co2

    @classmethod
    def waste_co2e_per_company(cls, company_id):
        waste_co2e_per_company = \
            cls.objects.filter(company_id=company_id).aggregate(total_co2=Sum('quantity_disposed'))[
                'total_co2'] or 0
        return waste_co2e_per_company

    def __str__(self):
        return f'{self.waste_name}'
