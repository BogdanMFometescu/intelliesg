import django_filters
from envdata.models import (Fuel, Energy, Sf6, Company, Refrigerant, Travel, Waste, NaturalGas, TaxonomyTurnover,
                            TaxonomySector, TaxonomyOpEx, TaxonomyCapEx,PurchasedGoodsAndServices,
                            CapitalGoods,
                            FuelEnergyRelatedActivities,
                            UpstreamTransportationAndDistribution,
                            EmployeeCommuting,
                            UpstreamLeasedAssets,
                            DownstreamTransportationAndDistribution,
                            ProcessingOfSoldProducts,
                            UseOfSoldProducts,
                            EndOfLifeTreatmentOfSoldProducts,
                            DownstreamLeasedAssets,
                            Franchises,
                            Investments)
from envdata.constants import *


class BaseTypeFilter(django_filters.FilterSet):
    year = django_filters.CharFilter(field_name='year', lookup_expr='exact')
    month = django_filters.ChoiceFilter(choices=MONTH, field_name='month')
    company = django_filters.ModelChoiceFilter(queryset=Company.objects.all())

    class Meta:
        abstract = True
        fields = ['company', 'year', 'month', ]


class FuelTypeFilter(BaseTypeFilter):
      class Meta(BaseTypeFilter.Meta):
          model = Fuel

class Sf6TypeFilter(BaseTypeFilter):
      class Meta(BaseTypeFilter.Meta):
          model = Sf6

class RefrigerantTypeFilter(BaseTypeFilter):
      class Meta(BaseTypeFilter.Meta):
          model = Refrigerant

class EnergyTypeFilter(BaseTypeFilter):
      class Meta(BaseTypeFilter.Meta):
          model = Energy

class TravelTypeFilter(BaseTypeFilter):
      class Meta(BaseTypeFilter.Meta):
          model = Travel

class WasteTypeFilter(BaseTypeFilter):
      class Meta(BaseTypeFilter.Meta):
          model = Waste

class NaturalGasTypeFilter(BaseTypeFilter):
      class Meta(BaseTypeFilter.Meta):
          model = NaturalGas

class TaxonomyTurnoverFilter(django_filters.FilterSet):
    company = django_filters.ModelChoiceFilter(queryset=Company.objects.all())
    turnover_activity = django_filters.ModelChoiceFilter(queryset=TaxonomySector.objects.all(), label='Activity')

    class Meta:
        model = TaxonomyTurnover
        fields = ['company', 'turnover_activity']

class TaxonomyOpeExFilter(django_filters.FilterSet):
    company = django_filters.ModelChoiceFilter(queryset=Company.objects.all())
    opex_activity = django_filters.ModelChoiceFilter(queryset=TaxonomySector.objects.all(), label='Activity')

    class Meta:
        model = TaxonomyOpEx
        fields = ['company', 'opex_activity']


class TaxonomyCapExFilter(django_filters.FilterSet):
    company = django_filters.ModelChoiceFilter(queryset=Company.objects.all())
    capex_activity = django_filters.ModelChoiceFilter(queryset=TaxonomySector.objects.all(), label='Activity')

    class Meta:
        model = TaxonomyCapEx
        fields = ['company', 'capex_activity']

class PurchasedGoodsFilter(BaseTypeFilter):
      class Meta(BaseTypeFilter.Meta):
          model = PurchasedGoodsAndServices

class CapitalGoodsFilter(BaseTypeFilter):
      class Meta(BaseTypeFilter.Meta):
          model = CapitalGoods

class FuelEnergyFilter(BaseTypeFilter):
      class Meta(BaseTypeFilter.Meta):
          model = FuelEnergyRelatedActivities

class UpstreanTDFilter(BaseTypeFilter):
      class Meta(BaseTypeFilter.Meta):
          model = UpstreamTransportationAndDistribution

class EmployeeCommutingFilter(BaseTypeFilter):
      class Meta(BaseTypeFilter.Meta):
          model = EmployeeCommuting

class UpstreamLAFilter(BaseTypeFilter):
      class Meta(BaseTypeFilter.Meta):
          model = UpstreamLeasedAssets

class DownstreamTDFilter(BaseTypeFilter):
      class Meta(BaseTypeFilter.Meta):
          model = DownstreamTransportationAndDistribution

class ProcessingOfSoldGoodsFilter(BaseTypeFilter):
      class Meta(BaseTypeFilter.Meta):
          model = ProcessingOfSoldProducts

class UseOfSoldProductsFilter(BaseTypeFilter):
      class Meta(BaseTypeFilter.Meta):
          model = UseOfSoldProducts

class EndOfLifeFilter(BaseTypeFilter):
      class Meta(BaseTypeFilter.Meta):
          model = EndOfLifeTreatmentOfSoldProducts

class DownstreamLAFilter(BaseTypeFilter):
      class Meta(BaseTypeFilter.Meta):
          model = DownstreamLeasedAssets

class FranchisesFilter(BaseTypeFilter):
      class Meta(BaseTypeFilter.Meta):
          model = Franchises

class InvestmentsFilter(BaseTypeFilter):
      class Meta(BaseTypeFilter.Meta):
          model = Investments
