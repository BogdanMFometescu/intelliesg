from django.db import models
import uuid


# Create your models here.

class Emission(models.Model):
    emission_type = models.CharField(max_length=255, blank=False, null=False)
    created = models.DateField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)


class ScopeOneEmission(models.Model):
    emission_type = models.ForeignKey(Emission, on_delete=models.CASCADE)
    calculation_method = models.CharField(max_length=255, blank=False, null=False)
    created = models.DateField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)


# SCOPE 1 emissions
class FuelEmission(models.Model):
    emission_type = models.ForeignKey(Emission, on_delete=models.CASCADE)
    emission_scope = models.ForeignKey(ScopeOneEmission, on_delete=models.CASCADE)
    fuel_type = models.CharField(max_length=255, blank=False, null=False)
    fuel_source = models.CharField(max_length=255, blank=False, null=False)
    fuel_quantity = models.FloatField(max_length=10, blank=False, null=False)
    pollution_norm = models.CharField(max_length=30, blank=False, null=False)
    activity_type = models.CharField(max_length=255, blank=False, null=False)
    vehicle_type = models.CharField(max_length=255, blank=False, null=False)
    measure_unit = models.CharField(max_length=30, blank=False, null=False)
    emission_factor = models.IntegerField(max_length=20, blank=False, null=False, default=0, )
    created = models.DateField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)


class Sf6Emission(models.Model):
    emission_type = models.ForeignKey(Emission, on_delete=models)
    emission_scope = models.ForeignKey(ScopeOneEmission, on_delete=models.CASCADE)
    equipment_type = models.CharField(max_length=255, blank=False, null=False)
    equipment_producer = models.CharField(max_length=255, blank=False, null=False)
    sf6_quantity = models.FloatField(max_length=10, blank=False, null=False)
    created = models.DateField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)


class RefrigerantEmission(models.Model):
    emission_type = models.ForeignKey(Emission, on_delete=models)
    emission_scope = models.ForeignKey(ScopeOneEmission, on_delete=models.CASCADE)
    equipment_type = models.CharField(max_length=255, blank=False, null=False)
    refrigerant_type = models.CharField(max_length=255, blank=False, null=False)
    refrigerant_quantity = models.FloatField(max_length=10, blank=False, null=False)
    created = models.DateField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)


# SCOPE 2 emissions
class ScopeTwoEmission(models.Model):
    emission_type = models.ForeignKey(Emission, on_delete=models.CASCADE)
    total_co2_scope_two = models.FloatField(blank=False, null=False)
    created = models.DateField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)


class EnergyAcquisition(models.Model):
    emission_type = models.ForeignKey(Emission, on_delete=models.CASCADE)
    emission_scope = models.ForeignKey(ScopeOneEmission, on_delete=models.CASCADE)
    location = models.CharField(max_length=255, blank=False, null=False)
    supplier_name = models.CharField(max_length=255, blank=False, null=False)
    measure_unit = models.CharField(max_length=20, blank=False, null=False)
    emission_factor = models.IntegerField(max_length=10, blank=False, null=True, default=0, )
    calculation_method = models.CharField(max_length=255, blank=False, null=False)
    created = models.DateField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)


# SCOPE 3 emissions

class ScopeThreeEmission(models.Model):
    emission_type = models.ForeignKey(Emission, on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)


@property
def co2e_for_fuel_emission(self):
    pass


@property
def co2_for_sf6_emission(self):
    pass


@property
def co2_for_energy_emission(self):
    pass


@property
def scope_one_emissions_total(self):
    pass


@property
def scope_two_emissions_total(self):
    pass
