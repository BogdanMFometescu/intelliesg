import django_filters
from socialdata.models import HealthAndSafety
from envdata.models import Company
from envdata.constants import *


class HealthAndSafetyFilter(django_filters.FilterSet):
    year = django_filters.CharFilter(field_name='year', lookup_expr='exact')
    month = django_filters.ChoiceFilter(choices=MONTH, field_name='month')
    company = django_filters.ModelChoiceFilter(queryset=Company.objects.all())

    class Meta:
        model = HealthAndSafety
        fields = ['company', 'year', 'month', ]