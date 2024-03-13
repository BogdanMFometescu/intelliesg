from django.db.models import F, FloatField, Sum
from django.db.models.functions import Cast

from envdata.models import Fuel, Sf6
from django.views.generic import TemplateView
from envdata.mixins import CompanyContextMixin


class Charts(TemplateView, CompanyContextMixin):
    template_name = 'emissions_charts.html'


class FuelEmissionsView(TemplateView):
    template_name = 'envdata/charts/fuel_chart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        annotated_qs = Fuel.objects.annotate(
            total_co2=Cast(F('fuel_quantity') * F('emission_factor'), output_field=FloatField())
        ).values('year', 'company__name').annotate(total_co2=Sum('total_co2')).order_by('year')

        years = sorted(list(set(annotated_qs.values_list('year', flat=True))))
        companies = {emission['company__name'] for emission in annotated_qs}
        data = {company: [0] * len(years) for company in companies}

        for emission in annotated_qs:
            year_index = years.index(emission['year'])
            data[emission['company__name']][year_index] = emission['total_co2']

        context['years'] = years
        context['data'] = data
        context['chart_title'] = 'Fuel Emissions by Year for All Companies'
        return context


class Sf6EmissionsView(TemplateView):
    template_name = 'envdata/charts/sf6_chart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        annotated_qs = Sf6.objects.annotate(
            total_co2=Cast(F('sf6_quantity') * F('emission_factor'), output_field=FloatField())
        ).values('year', 'company__name').annotate(total_co2=Sum('total_co2')).order_by('year')

        years = sorted(list(set(annotated_qs.values_list('year', flat=True))))
        companies = {emission['company__name'] for emission in annotated_qs}
        data = {company: [0] * len(years) for company in companies}

        for emission in annotated_qs:
            year_index = years.index(emission['year'])
            data[emission['company__name']][year_index] = emission['total_co2']

        context['years'] = years
        context['data'] = data
        context['chart_title'] = 'Sf6 Emissions by Year for All Companies'
        return context
