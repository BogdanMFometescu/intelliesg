from django.db import models
from django.db.models import Sum, F
import uuid
from envdata.constants import *
from users.models import Profile
from common.models import BaseIdentifierClass
from companies.models import Company



class BaseEmissionClass(BaseIdentifierClass):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    month = models.CharField(blank=False, null=False, choices=MONTH,max_length=255)
    year = models.CharField(blank=False, null=False, max_length=4)
    emission_type = models.CharField(max_length=255, blank=False, null=False, choices=EMISSION_TYPE)
    emission_scope = models.CharField(max_length=255, blank=False, null=False, choices=EMISSION_SCOPE)
    quantity = models.FloatField(max_length=20,null=False,blank=False,default=0)
    emission_factor = models.FloatField(blank=False, null=False, default=0,)
    measure_unit = models.CharField(max_length=25,null=False,blank=False,choices=MEASURE_UNITS)


    @property
    def calculate_emissions(self):
        return self.emission_factor*self.quantity

    @classmethod
    def total_emissions(cls, company_id):
        emissions = \
            cls.objects.filter(company_id=company_id).aggregate(
                total_emissions=Sum(F('quantity') * F('emission_factor')))[
                'total_emissions'] or 0
        return emissions

    @classmethod
    def annual_emissions(cls, company_id):
        annual_emissions = cls.objects.filter(company_id=company_id).values('year', 'month').annotate(
            total_co2=Sum(F('quantity') * F('emission_factor'))).order_by('year', 'month')
        return annual_emissions

    class Meta:
        abstract = True


# SCOPE 1 emissions
class Fuel(BaseEmissionClass):
    fuel_type = models.CharField(max_length=255, blank=False, null=False, choices=FUEL_TYPE)
    fuel_source = models.CharField(max_length=255, blank=False, null=False)
    pollution_norm = models.CharField(max_length=30, blank=False, null=False, choices=POLLUTION_NORM)
    activity_type = models.CharField(max_length=255, blank=False, null=False, choices=ACTIVITY_TYPE)
    vehicle_type = models.CharField(max_length=255, blank=False, null=False, choices=VEHICLE_TYPE)

    class Meta :
        verbose_name = "Fuel"
        verbose_name_plural = "Fuels"

class NaturalGas(BaseEmissionClass):
    location = models.CharField(max_length=255, blank=False, null=False, choices=NATURAL_GAS_LOCATIONS)

    class Meta:
        verbose_name = "Natural Gas"
        verbose_name_plural = "Natural Gases"


class Sf6(models.Model):
    equipment_type = models.CharField(max_length=255, blank=False, null=False)
    equipment_producer = models.CharField(max_length=255, blank=False, null=False)

    class Meta:
        verbose_name ="HexaSulfurFluoride"
        verbose_name_plural = "HexaSulfurFluoride"
  

class Refrigerant(BaseEmissionClass):
    refrigerant_type = models.CharField(max_length=255, blank=False, null=False)

    class Meta:
        verbose_name = "Refrigerant"
        verbose_name_plural = "Refrigerants"
   

# SCOPE 2 emissions
class Energy(BaseEmissionClass):
    location = models.CharField(max_length=255, blank=False, choices=ENERGY_LOCATIONS)
    supplier_name = models.CharField(max_length=255, blank=False, null=False)
    calculation_method = models.CharField(max_length=255, blank=False, choices=CALCULATION_METHOD)

    class Meta:
        verbose_name = "Energy Aquisition"
        verbose_name_plural = "Energy Aquisitions"
   

# SCOPE 3 emissions
class Travel(BaseEmissionClass):
    origin = models.CharField(max_length=255, blank=False, null=False)
    destination = models.CharField(max_length=255, blank=False, null=False)
    distance = models.FloatField(blank=False, null=False)
    fuel_consumption = models.FloatField(blank=False, null=False, default=7.5)


    class Meta:
        verbose_name = "Travel"
        verbose_name_plural = "Travels"


class Waste(BaseEmissionClass):
    waste_name = models.CharField(max_length=255, blank=False, null=False)
    quantity_recycled = models.FloatField(blank=False, null=False)
    quantity_disposed = models.FloatField(blank=False, null=False)
    quantity_land_filled = models.FloatField(blank=False, null=False)
    emission_factor = models.FloatField(blank=False, null=True, default=0, )

  

class PurchasedGoodsAndServices(BaseEmissionClass):
   pass


class CapitalGoods(BaseEmissionClass):
   pass


class FuelEnergyRelatedActivities(BaseEmissionClass):
    pass


class UpstreamTransportationAndDistribution(BaseEmissionClass):
    pass
    


class EmployeeCommuting(BaseEmissionClass):
    pass



class UpstreamLeasedAssets (BaseEmissionClass):
    pass



class DownstreamTransportationAndDistribution(BaseEmissionClass):
    pass


class ProcessingOfSoldProducts(BaseEmissionClass):
    pass

class UseOfSoldProducts(BaseEmissionClass):
    pass


class EndOfLifeTreatmentOfSoldProducts(BaseEmissionClass):
    pass



class DownstreamLeasedAssets(BaseEmissionClass):
    pass


class Franchises(BaseEmissionClass):
    pass

class Investments(BaseEmissionClass):
    pass



#CO2 SBTi and NET ZERO Targets 

class Target(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
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

#EU TAXONOMY
class TaxonomySector(BaseIdentifierClass):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    sector = models.CharField(blank=False, null=False, choices=TAXONOMY_SECTOR_CHOICES, max_length=2000)
    activity = models.CharField(blank=False, null=False, choices=TAXONOMY_ACTIVITY_CHOICES,max_length=255)
    activity_type = models.CharField(blank=False, null=False, choices=TAXONOMY_ACTIVITY_TYPE_CHOICES, max_length=255, )
    nace_code = models.FloatField(blank=False, null=False, default=0.0)


    def __str__(self):
        return f'{self.activity}'

class TaxonomyTurnover(BaseIdentifierClass):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    turnover_activity = models.ForeignKey(TaxonomySector, on_delete=models.CASCADE)
    currency = models.CharField(blank=False, null=False, choices=CURRENCY_CHOICES, max_length=10)

    total_turnover = models.FloatField(blank=True, null=True, default=0.0)
    turnover_eligible = models.FloatField(blank=True, null=True, default=0.0)
    turnover_aligned = models.FloatField(blank=True, null=True, default=0.0)
    turnover_non_eligible = models.FloatField(blank=True, null=True, default=0.0)

    climate_change_adaptation = models.FloatField(blank=False, null=False, max_length=10)
    climate_change_mitigation = models.FloatField(blank=False, null=False, max_length=10)

    climate_change_dnsh = models.CharField(blank=False, null=False, max_length=255, choices=DNSH_CHOICES)
    marine_resources_dnsh = models.CharField(blank=False, null=False, max_length=255, choices=DNSH_CHOICES)
    circular_economy_dnsh = models.CharField(blank=False, null=False, max_length=255, choices=DNSH_CHOICES)
    pollution_dnsh = models.CharField(blank=False, null=False, max_length=255, choices=DNSH_CHOICES)
    biodiversity_dnsh = models.CharField(blank=False, null=False, max_length=255, choices=DNSH_CHOICES)

    @property
    def get_eligible_percent(self):
        return ((self.turnover_eligible / self.total_turnover) * 100).__round__(2)

    @property
    def get_aligned_percent(self):
        return ((self.turnover_aligned / self.total_turnover) * 100).__round__(2)

    @property
    def get_non_eligible_percent(self):
        return ((self.turnover_non_eligible / self.total_turnover) * 100).__round__(2)


    def __str__(self):
        return f'{self.total_turnover}'


class TaxonomyCapEx(BaseIdentifierClass):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    capex_activity = models.ForeignKey(TaxonomySector, on_delete=models.CASCADE)
    currency = models.CharField(blank=False, null=False, choices=CURRENCY_CHOICES, max_length=10)

    total_capex = models.FloatField(blank=True, null=True, default=0.0)
    capex_eligible = models.FloatField(blank=True, null=True, default=0.0)
    capex_aligned = models.FloatField(blank=True, null=True, default=0.0)
    capex_non_eligible = models.FloatField(blank=True, null=True, default=0.0)

    climate_change_dnsh = models.CharField(blank=False, null=False, max_length=255, choices=DNSH_CHOICES)
    marine_resources_dnsh = models.CharField(blank=False, null=False, max_length=255, choices=DNSH_CHOICES)
    circular_economy_dnsh = models.CharField(blank=False, null=False, max_length=255, choices=DNSH_CHOICES)
    pollution_dnsh = models.CharField(blank=False, null=False, max_length=255, choices=DNSH_CHOICES)
    biodiversity_dnsh = models.CharField(blank=False, null=False, max_length=255, choices=DNSH_CHOICES)

    @property
    def get_eligible_percent(self):
        return ((self.capex_eligible / self.total_capex) * 100).__round__(2)

    @property
    def get_aligned_percent(self):
        return ((self.capex_aligned / self.total_capex) * 100).__round__(2)

    @property
    def get_non_eligible_percent(self):
        return ((self.capex_non_eligible / self.total_capex) * 100).__round__(2)

    def __str__(self):
        return f'{self.total_capex}'


class TaxonomyOpEx(BaseIdentifierClass):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    opex_activity = models.ForeignKey(TaxonomySector, on_delete=models.CASCADE)
    currency = models.CharField(blank=False, null=False, choices=CURRENCY_CHOICES, max_length=10)

    total_opex = models.FloatField(blank=True, null=True, default=0.0)
    opex_eligible = models.FloatField(blank=True, null=True, default=0.0)
    opex_aligned = models.FloatField(blank=True, null=True, default=0.0)
    opex_non_eligible = models.FloatField(blank=True, null=True, default=0.0)

    climate_change_dnsh = models.CharField(blank=False, null=False, max_length=255, choices=DNSH_CHOICES)
    marine_resources_dnsh = models.CharField(blank=False, null=False, max_length=255, choices=DNSH_CHOICES)
    circular_economy_dnsh = models.CharField(blank=False, null=False, max_length=255, choices=DNSH_CHOICES)
    pollution_dnsh = models.CharField(blank=False, null=False, max_length=255, choices=DNSH_CHOICES)
    biodiversity_dnsh = models.CharField(blank=False, null=False, max_length=255, choices=DNSH_CHOICES)



    @property
    def get_eligible_percent(self):
        return ((self.opex_eligible / self.total_opex) * 100).__round__(2)

    @property
    def get_aligned_percent(self):
        return ((self.opex_aligned / self.total_opex) * 100).__round__(2)

    @property
    def get_non_eligible_percent(self):
        return ((self.opex_non_eligible / self.total_opex) * 100).__round__(2)

    def __str__(self):
        return f'{self.total_opex}'
