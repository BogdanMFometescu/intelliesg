import django_filters
from envdata.models import (Fuel, Energy, Sf6, Company, Refrigerant, Travel, Waste, NaturalGas, TaxonomyTurnover,TaxonomySector)
from envdata.constants import *


class FuelTypeFilter(django_filters.FilterSet):
    year = django_filters.CharFilter(field_name='year', lookup_expr='exact')
    month = django_filters.ChoiceFilter(choices=MONTH, field_name='month')
    company = django_filters.ModelChoiceFilter(queryset=Company.objects.all())

    class Meta:
        model = Fuel
        fields = ['company', 'year', 'month', ]


class Sf6TypeFilter(django_filters.FilterSet):
    year = django_filters.CharFilter(field_name='year', lookup_expr='exact')
    month = django_filters.ChoiceFilter(choices=MONTH, field_name='month')
    company = django_filters.ModelChoiceFilter(queryset=Company.objects.all())

    class Meta:
        model = Sf6
        fields = ['company', 'year', 'month', ]


class RefrigerantTypeFilter(django_filters.FilterSet):
    year = django_filters.CharFilter(field_name='year', lookup_expr='exact')
    month = django_filters.ChoiceFilter(choices=MONTH, field_name='month')
    company = django_filters.ModelChoiceFilter(queryset=Company.objects.all())

    class Meta:
        model = Refrigerant
        fields = ['company', 'year', 'month', ]


class EnergyTypeFilter(django_filters.FilterSet):
    year = django_filters.CharFilter(field_name='year', lookup_expr='exact')
    month = django_filters.ChoiceFilter(choices=MONTH, field_name='month')
    company = django_filters.ModelChoiceFilter(queryset=Company.objects.all())

    class Meta:
        model = Energy
        fields = ['company', 'year', 'month', ]


class TravelTypeFilter(django_filters.FilterSet):
    year = django_filters.CharFilter(field_name='year', lookup_expr='exact')
    month = django_filters.ChoiceFilter(choices=MONTH, field_name='month')
    company = django_filters.ModelChoiceFilter(queryset=Company.objects.all())

    class Meta:
        model = Travel
        fields = ['company', 'year', 'month', ]


class WasteTypeFilter(django_filters.FilterSet):
    year = django_filters.CharFilter(field_name='year', lookup_expr='exact')
    month = django_filters.ChoiceFilter(choices=MONTH, field_name='month')
    company = django_filters.ModelChoiceFilter(queryset=Company.objects.all())

    class Meta:
        model = Waste
        fields = ['company', 'year', 'month', ]


class NaturalGasTypeFilter(django_filters.FilterSet):
    year = django_filters.CharFilter(field_name='year', lookup_expr='exact')
    month = django_filters.ChoiceFilter(choices=MONTH, field_name='month')
    company = django_filters.ModelChoiceFilter(queryset=Company.objects.all())

    class Meta:
        model = NaturalGas
        fields = ['company', 'year', 'month', ]


class TaxonomyTurnoverFilter(django_filters.FilterSet):
    company = django_filters.ModelChoiceFilter(queryset=Company.objects.all())
    turnover_activity = django_filters.ModelChoiceFilter(queryset=TaxonomySector.objects.all(),label='Activity')

    class Meta:
        model = TaxonomyTurnover
        fields = ['company','turnover_activity' ]
