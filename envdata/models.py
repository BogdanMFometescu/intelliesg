from django.db import models
from django.db.models import Sum, F
import uuid
from envdata.constants import *
from users.models import Profile


class Company(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='companies', null=True, blank=True)
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
        gas_co2e = NaturalGas.gas_co2e_per_company(self.id)
        travel_co2e = Travel.travel_co2e_per_company(self.id)
        energy_co2e = Energy.energy_co2e_per_company(self.id)
        waste_co2e = Waste.waste_co2e_per_company(self.id)

        total_co2e = sum([fuel_co2e, refrigerant_co2e, sf6_co2e, travel_co2e, energy_co2e, waste_co2e, gas_co2e])
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
    def gas_co2e(self):
        return NaturalGas.gas_co2e_per_company(self.id)

    @property
    def travel_co2e(self):
        return Travel.travel_co2e_per_company(self.id)

    @property
    def energy_co2e(self):
        return Energy.energy_co2e_per_company(self.id)

    @property
    def waste_co2e(self):
        return Waste.waste_co2e_per_company(self.id)

    @property
    def co2e_net_zero_target(self):
        return Target.get_co2_net_zero_target(self.id)

    def __str__(self):
        return self.name


# SCOPE 1 emissions
class Fuel(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    month = models.CharField(blank=False, null=False, choices=MONTH)
    year = models.CharField(blank=False, null=False, max_length=4)
    emission_type = models.CharField(max_length=255, blank=False, null=False, choices=EMISSION_TYPE)
    emission_scope = models.CharField(max_length=255, blank=False, null=False, choices=EMISSION_SCOPE)
    fuel_type = models.CharField(max_length=255, blank=False, null=False, choices=FUEL_TYPE)
    fuel_source = models.CharField(max_length=255, blank=False, null=False)
    fuel_quantity = models.FloatField(max_length=10, blank=False, null=False, default=0.00)
    pollution_norm = models.CharField(max_length=30, blank=False, null=False, choices=POLLUTION_NORM)
    activity_type = models.CharField(max_length=255, blank=False, null=False, choices=ACTIVITY_TYPE)
    vehicle_type = models.CharField(max_length=255, blank=False, null=False, choices=VEHICLE_TYPE)
    measure_unit = models.CharField(max_length=30, blank=False, null=False, default='L')
    emission_factor = models.FloatField(blank=False, null=False, default=0, )
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

    @classmethod
    def annual_co2_per_company(cls, company_id):
        annual_co2_per_company = cls.objects.filter(company_id=company_id).values('year', 'month').annotate(
            total_co2=Sum(F('fuel_quantity') * F('emission_factor'))).order_by('year', 'month')
        return annual_co2_per_company

    def __str__(self):
        return f'{self.fuel_type}'


class NaturalGas(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    month = models.CharField(blank=False, null=False, choices=MONTH)
    year = models.CharField(blank=False, null=False, max_length=4)
    emission_type = models.CharField(max_length=255, blank=False, null=False, choices=EMISSION_TYPE)
    emission_scope = models.CharField(max_length=255, blank=False, null=False, choices=EMISSION_SCOPE)
    location = models.CharField(max_length=255, blank=False, null=False, choices=NATURAL_GAS_LOCATIONS)
    gas_quantity = models.FloatField(max_length=10, blank=False, null=False, default=0)
    emission_factor = models.FloatField(blank=False, null=False, default=0, )
    measure_unit = models.CharField(max_length=30, blank=False, null=False, default='kWh')
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    @property
    def co2_for_natural_gas_emission(self):
        total_co2 = self.gas_quantity * self.emission_factor
        return total_co2

    @classmethod
    def gas_co2e_per_company(cls, company_id):
        gas_co2e_per_company = \
            cls.objects.filter(company=company_id).aggregate(total_co2=Sum(F('gas_quantity') * F('emission_factor')))[
                'total_co2'] or 0
        return gas_co2e_per_company

    @classmethod
    def annual_co2_per_company(cls, company_id):
        annual_co2_per_company = cls.objects.filter(company_id=company_id).values('year', 'month').annotate(
            total_co2=Sum(F('gas_quantity') * F('emission_factor'))).order_by('year', 'month')
        return annual_co2_per_company

    def __str__(self):
        return f'{self.location}'


class Sf6(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    month = models.CharField(blank=False, null=False, choices=MONTH)
    year = models.CharField(blank=False, null=False, max_length=4)
    emission_type = models.CharField(max_length=255, blank=False, null=False, choices=EMISSION_TYPE)
    emission_scope = models.CharField(max_length=255, blank=False, null=False, choices=EMISSION_SCOPE)
    equipment_type = models.CharField(max_length=255, blank=False, null=False)
    equipment_producer = models.CharField(max_length=255, blank=False, null=False)
    sf6_quantity = models.FloatField(max_length=10, blank=False, null=False)
    emission_factor = models.FloatField(blank=False, null=False, default=0, )
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)

    @property
    def co2e_for_sf6_emission(self):
        total_co2 = self.sf6_quantity * self.emission_factor
        return total_co2

    @classmethod
    def sf6_co2e_per_company(cls, company_id):
        sf6_co2e_per_company = \
            cls.objects.filter(company=company_id).aggregate(total_co2=Sum(F('sf6_quantity') * F('emission_factor')))[
                'total_co2'] or 0
        return sf6_co2e_per_company

    @classmethod
    def annual_co2_per_company(cls, company_id):
        annual_co2_per_company = cls.objects.filter(company_id=company_id).values('year', 'month').annotate(
            total_co2=Sum(F('sf6_quantity') * F('emission_factor'))).order_by('year', 'month')
        return annual_co2_per_company


class Refrigerant(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    month = models.CharField(blank=False, null=False, choices=MONTH)
    year = models.CharField(blank=False, null=False, max_length=4)
    emission_type = models.CharField(max_length=255, blank=False, null=False, choices=EMISSION_TYPE)
    emission_scope = models.CharField(max_length=255, blank=False, null=False, choices=EMISSION_SCOPE)
    refrigerant_type = models.CharField(max_length=255, blank=False, null=False)
    refrigerant_quantity = models.FloatField(max_length=10, blank=False, null=False, default=0.00)
    emission_factor = models.FloatField(blank=False, null=False, default=0, )
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

    @classmethod
    def annual_co2_per_company(cls, company_id):
        annual_co2_per_company = cls.objects.filter(company_id=company_id).values('year', 'month').annotate(
            total_co2=Sum(F('refrigerant_quantity') * F('emission_factor'))).order_by('year', 'month')
        return annual_co2_per_company

    def __str__(self):
        return f'{self.refrigerant_type}'


# SCOPE 2 emissions


class Energy(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    month = models.CharField(blank=False, null=False, choices=MONTH)
    year = models.CharField(blank=False, null=False, max_length=4)
    emission_type = models.CharField(max_length=255, blank=False, null=False, choices=EMISSION_TYPE)
    emission_scope = models.CharField(max_length=255, blank=False, null=False, choices=EMISSION_SCOPE)
    location = models.CharField(max_length=255, blank=False, choices=ENERGY_LOCATIONS)
    supplier_name = models.CharField(max_length=255, blank=False, null=False)
    measure_unit = models.CharField(max_length=20, blank=False, null=False)
    energy_quantity = models.FloatField(max_length=20, blank=False, null=False, default=0.00)
    emission_factor = models.FloatField(blank=False, null=True, default=0, )
    calculation_method = models.CharField(max_length=255, blank=False, choices=CALCULATION_METHOD)
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

    @classmethod
    def annual_co2_per_company(cls, company_id):
        annual_co2_per_company = cls.objects.filter(company_id=company_id).values('year', 'month').annotate(
            total_co2=Sum(F('energy_quantity') * F('emission_factor'))).order_by('year', 'month')
        return annual_co2_per_company

    def __str__(self):
        return f'{self.supplier_name}'


# SCOPE 3 emissions


class Travel(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    month = models.CharField(blank=False, null=False, choices=MONTH)
    year = models.CharField(blank=False, null=False, max_length=4)
    emission_type = models.CharField(max_length=255, blank=False, null=False, choices=EMISSION_TYPE)
    emission_scope = models.CharField(max_length=255, blank=False, null=False, choices=EMISSION_SCOPE)
    origin = models.CharField(max_length=255, blank=False, null=False)
    destination = models.CharField(max_length=255, blank=False, null=False)
    emission_factor = models.FloatField(blank=False, null=True, default=0, )
    distance = models.FloatField(blank=False, null=False)
    fuel_consumption = models.FloatField(blank=False, null=False, default=7.5)

    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)

    @property
    def co2_for_distance_calculation(self):
        total_co2 = ((self.distance * self.fuel_consumption) / 100) * 10.8
        return total_co2.__round__(2)

    @classmethod
    def travel_co2e_per_company(cls, company_id):
        travel_co2_per_company = cls.objects.filter(company_id=company_id).aggregate(
            total_co2=Sum(F('distance') * F('emission_factor')))[
                                     'total_co2'] or 0
        return travel_co2_per_company

    @classmethod
    def annual_co2_per_company(cls, company_id):
        annual_co2_per_company = cls.objects.filter(company_id=company_id).values('year', 'month').annotate(
            total_co2=Sum(F('distance') * F('emission_factor'))).order_by('year', 'month')
        return annual_co2_per_company

    def __str__(self):
        return f'{self.distance}'


class Waste(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    month = models.CharField(blank=False, null=False, choices=MONTH)
    year = models.CharField(blank=False, null=False, max_length=4)
    emission_type = models.CharField(max_length=255, blank=False, null=False, choices=EMISSION_TYPE)
    emission_scope = models.CharField(max_length=255, blank=False, null=False, choices=EMISSION_SCOPE)
    waste_name = models.CharField(max_length=255, blank=False, null=False)
    quantity_recycled = models.FloatField(blank=False, null=False)
    quantity_disposed = models.FloatField(blank=False, null=False)
    quantity_land_filled = models.FloatField(blank=False, null=False)
    emission_factor = models.FloatField(blank=False, null=True, default=0, )
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

    @classmethod
    def annual_co2_per_company(cls, company_id):
        annual_co2_per_company = cls.objects.filter(company_id=company_id).values('year', 'month').annotate(
            total_co2=Sum(F('quantity_disposed') * F('emission_factor'))).order_by('year', 'month')
        return annual_co2_per_company

    def __str__(self):
        return f'{self.waste_name}'


class Target(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    base_year = models.IntegerField(null=True, blank=True, default=2019)
    net_zero_year = models.IntegerField(null=True, blank=True, default=2050)
    intermediate_year = models.IntegerField(null=True, blank=True)
    co2e_base_year = models.IntegerField(null=False, blank=False, default=0)
    reduction_percentage = models.FloatField(null=False, blank=False, default=1)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, unique=True)

    @classmethod
    def get_co2_net_zero_target(cls, company_id):
        target = cls.objects.filter(company_id=company_id, intermediate_year=2050).first()
        if target is not None:
            net_zero_target = (target.co2e_base_year * target.reduction_percentage) / 100
            return target.co2e_base_year - net_zero_target
        return 0

    @classmethod
    def get_target_per_year(cls, company_id):
        targets = cls.objects.filter(company_id=company_id)
        target_dict = {}
        for target in targets:
            target_value = target.co2e_base_year - (target.co2e_base_year * (target.reduction_percentage / 100))
            target_dict[target.intermediate_year] = target_value
        return target_dict

    @property
    def co2e_year_target(self):
        target = (self.co2e_base_year * self.reduction_percentage) / 100
        return self.co2e_base_year - target

    def __str__(self):
        return f'{self.co2e_base_year}'


class TaxonomySector(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    sector = models.CharField(blank=False, null=False, choices=TAXONOMY_SECTOR_CHOICES, max_length=2000)
    activity = models.CharField(blank=False, null=False, choices=TAXONOMY_ACTIVITY_CHOICES, max_length=2000)
    nace_code = models.FloatField(blank=False, null=False, default=0.0)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.sector}'

    class Meta:
        verbose_name = 'Taxonomy Sector'
        verbose_name_plural = 'Taxonomy Sectors'


class TaxonomyTurnover(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    sector = models.ForeignKey(TaxonomySector, on_delete=models.CASCADE)
    currency = models.CharField(blank=False, null=False, choices=CURRENCY_CHOICES, max_length=10)
    turnover = models.FloatField(blank=False, null=False, default=0.0)

    eligible_activity = models.CharField(blank=False, null=False, max_length=1000)
    eligible_activity_amount = models.FloatField(blank=False, null=False, default=0.0)

    aligned_activity = models.CharField(blank=False, null=False, max_length=1000)
    aligned_activity_amount = models.FloatField(blank=False, null=False, default=0.0)

    not_aligned_activity = models.CharField(blank=False, null=False, max_length=1000)
    not_aligned_activity_amount = models.FloatField(blank=False, null=False, default=0.0)

    climate_change_mitigation = models.FloatField(blank=False, null=False, max_length=255, default=0.0)
    climate_change_adaptation = models.FloatField(blank=False, null=False, max_length=255, default=0.0)

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    @property
    def get_eligible_turnover(self):
        return (self.eligible_activity_amount / self.turnover) * 100

    @property
    def get_aligned_turnover(self):
        return (self.aligned_activity_amount / self.turnover) * 100

    @property
    def get_non_aligned_turnover(self):
        return (self.not_aligned_activity_amount / self.turnover) * 100

    @property
    def get_total_aligned_turnover(self):
        return self.get_eligible_turnover + self.get_aligned_turnover

    @property
    def get_aligned_turnover_percent(self):
        aligned_amount = self.get_total_aligned_turnover
        return (aligned_amount / self.turnover) * 100

    def __str__(self):
        return f'{self.turnover}'


class TaxonomyCapEx(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    sector = models.ForeignKey(TaxonomySector, on_delete=models.CASCADE)
    currency = models.CharField(blank=False, null=False, choices=CURRENCY_CHOICES, max_length=10)
    capex = models.FloatField(blank=False, null=False, default=0.0)

    capex_a_activity = models.CharField(blank=False, null=False, max_length=1000)
    capex_a_amount = models.FloatField(blank=False, null=False, default=0.0)

    capex_b_activity = models.CharField(blank=False, null=False, max_length=1000)
    capex_b_amount = models.FloatField(blank=False, null=False, default=0.0)

    capex_c_activity = models.CharField(blank=False, null=False, max_length=1000)
    capex_c_amount = models.FloatField(blank=False, null=False, default=0.0)

    climate_change_mitigation = models.FloatField(blank=False, null=False, max_length=255, default=0.0)
    climate_change_adaptation = models.FloatField(blank=False, null=False, max_length=255, default=0.0)

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    @property
    def get_aligned_capex_a(self):
        return (self.capex_a_amount / self.capex) * 100

    @property
    def get_aligned_capex_b(self):
        return (self.capex_b_amount / self.capex) * 100

    @property
    def get_aligned_capex_c(self):
        return (self.capex_c_amount / self.capex) * 100

    @property
    def get_aligned_total_capex(self):
        return self.get_aligned_capex_a + self.get_aligned_capex_b + self.get_aligned_capex_c

    @property
    def get_aligned_capex_percent(self):
        aligned_amount = self.get_aligned_total_capex
        return (aligned_amount / self.capex) * 100


def __str__(self):
    return f'{self.capex}'


class TaxonomyOpEx(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    sector = models.ForeignKey(TaxonomySector, on_delete=models.CASCADE)
    currency = models.CharField(blank=False, null=False, choices=CURRENCY_CHOICES, max_length=10)
    opex = models.FloatField(blank=False, null=False, default=0.0)

    opex_a_activity = models.CharField(blank=False, null=False, max_length=1000)
    opex_a_amount = models.FloatField(blank=False, null=False, default=0.0)

    opex_b_activity = models.CharField(blank=False, null=False, max_length=1000)
    opex_b_amount = models.FloatField(blank=False, null=False, default=0.0)

    opex_c_activity = models.CharField(blank=False, null=False, max_length=1000)
    opex_c_amount = models.FloatField(blank=False, null=False, default=0.0)

    climate_change_mitigation = models.FloatField(blank=False, null=False, max_length=255, default=0.0)
    climate_change_adaptation = models.FloatField(blank=False, null=False, max_length=255, default=0.0)

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    @property
    def get_aligned_opex_a(self):
        return (self.opex_a_amount / self.opex) * 100

    @property
    def get_aligned_opex_b(self):
        return (self.opex_b_amount / self.opex) * 100

    @property
    def get_aligned_opex_c(self):
        return (self.opex_c_amount / self.opex) * 100

    @property
    def get_aligned_total_opex(self):
        return self.get_aligned_opex_a + self.get_aligned_opex_b + self.get_aligned_opex_c

    @property
    def get_aligned_opex_percent(self):
        aligned_amount = self.get_aligned_total_opex
        return (aligned_amount / self.opex) * 100

    def __str__(self):
        return f'{self.opex}'


class DoNotSeriousHarm(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    sector = models.ForeignKey(TaxonomySector, on_delete=models.CASCADE)
    climate_change_turnover = models.CharField(blank=False, null=False, max_length=255, choices=DNSH_CHOICES)
    climate_change_capex = models.CharField(blank=False, null=False, max_length=255, choices=DNSH_CHOICES)
    climate_change_opex = models.CharField(blank=False, null=False, max_length=255, choices=DNSH_CHOICES)

    marine_resources_turnover = models.CharField(blank=False, null=False, max_length=255, choices=DNSH_CHOICES)
    marine_resources_capex = models.CharField(blank=False, null=False, max_length=255, choices=DNSH_CHOICES)
    marine_resources_opex = models.CharField(blank=False, null=False, max_length=255, choices=DNSH_CHOICES)

    circular_economy_turnover = models.CharField(blank=False, null=False, max_length=255, choices=DNSH_CHOICES)
    circular_economy_capex = models.CharField(blank=False, null=False, max_length=255, choices=DNSH_CHOICES)
    circular_economy_opex = models.CharField(blank=False, null=False, max_length=255, choices=DNSH_CHOICES)

    pollution_turnover = models.CharField(blank=False, null=False, max_length=255, choices=DNSH_CHOICES)
    pollution_capex = models.CharField(blank=False, null=False, max_length=255, choices=DNSH_CHOICES)
    pollution_opex = models.CharField(blank=False, null=False, max_length=255, choices=DNSH_CHOICES)

    biodiversity_turnover = models.CharField(blank=False, null=False, max_length=255, choices=DNSH_CHOICES)
    biodiversity_capex = models.CharField(blank=False, null=False, max_length=255, choices=DNSH_CHOICES)
    biodiversity_opex = models.CharField(blank=False, null=False, max_length=255, choices=DNSH_CHOICES)

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.sector}'
