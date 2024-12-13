import django_filters
from socialdata.models import (HealthAndSafety, EmployeeByContracts, NewEmployeeByAge,
                               RotationRateOfEmployeeByAge, RetirementRate)
from companies.models import Company
from envdata.constants import *


class HealthAndSafetyFilter(django_filters.FilterSet):
    year = django_filters.CharFilter(field_name='year', lookup_expr='exact')
    month = django_filters.ChoiceFilter(choices=MONTH, field_name='month')
    company = django_filters.ModelChoiceFilter(queryset=Company.objects.all())

    class Meta:
        model = HealthAndSafety
        fields = ['company', 'year', 'month', ]


class EmployeeContractsFilter(django_filters.FilterSet):
    year = django_filters.CharFilter(field_name='year', lookup_expr='exact')
    company = django_filters.ModelChoiceFilter(queryset=Company.objects.all())
    county = django_filters.ChoiceFilter(choices=COUNTY_CHOICES, field_name='county')

    class Meta:
        model = EmployeeByContracts
        fields = ['company', 'year', 'county']


class NewEmployeeByAgeFilter(django_filters.FilterSet):
    year = django_filters.CharFilter(field_name='year', lookup_expr='exact')
    company = django_filters.ModelChoiceFilter(queryset=Company.objects.all())
    county = django_filters.ChoiceFilter(choices=COUNTY_CHOICES, field_name='county')

    class Meta:
        model = NewEmployeeByAge
        fields = ['company', 'year', 'county']


class RotationRateFilter(django_filters.FilterSet):
    year = django_filters.CharFilter(field_name='year', lookup_expr='exact')
    company = django_filters.ModelChoiceFilter(queryset=Company.objects.all())
    county = django_filters.ChoiceFilter(choices=COUNTY_CHOICES, field_name='county')

    class Meta:
        model = RotationRateOfEmployeeByAge
        fields = ['company', 'year', 'county']


class RetirementRateFilter(django_filters.FilterSet):
    year = django_filters.CharFilter(field_name='year', lookup_expr='exact')
    company = django_filters.ModelChoiceFilter(queryset=Company.objects.all())
    county = django_filters.ChoiceFilter(choices=COUNTY_CHOICES, field_name='county')

    class Meta:
        model = RetirementRate
        fields = ['company', 'year', 'county']
