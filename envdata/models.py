from django.db import models
import uuid


# Create your models here.

class CarbonFootprint(models.Model):
    emission_type = models.CharField(max_length=255, blank=False, null=False)
    created = models.DateField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)


class ScopeOneEmission(models.Model):
    emission_type = models.ForeignKey(CarbonFootprint, on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)


class FuelEmission(models.Model):
    emission_type = models.ForeignKey(CarbonFootprint, on_delete=models.CASCADE)
    emission_scope = models.ForeignKey(ScopeOneEmission, on_delete=models.CASCADE)
    fuel_type = models.CharField(max_length=255, blank=False, null=False)
    fuel_source = models.CharField(max_length=255, blank=False, null=False)
    pollution_norm = models.CharField(max_length=30, blank=False, null=False)
    activity_type = models.CharField(max_length=255, blank=False, null=False)
    vehicle_type = models.CharField(max_length=255, blank=False, null=False)
    measure_unit = models.CharField(max_length=30, blank=False, null=False)
    fuel_quantity = models.FloatField(max_length=10, blank=False, null=False)
    created = models.DateField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)


class ScopeTwoEmission(models.Model):
    emission_type = models.ForeignKey(CarbonFootprint, on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)


class ScopeThreeEmission(models.Model):
    emission_type = models.ForeignKey(CarbonFootprint, on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)


@property
def calculate_emission_factor():
    pass


@property
def calculate_co2_emission_factor():
    pass
