from django.db.models import F, FloatField, Sum
from django.db.models.functions import Cast
import json
from envdata.models import Fuel, Sf6, Refrigerant, Energy, Waste, Travel, NaturalGas
from django.views.generic import TemplateView
from common.mixins import CompanyContextMixin


class Charts(TemplateView, CompanyContextMixin):
    template_name = 'emissions_charts.html'


class FuelEmissionsView(TemplateView):
    template_name = 'envdata/charts/display_charts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Aggregate emissions by year and month
        annotated_qs = Fuel.objects.annotate(
            total_co2=Cast(F('quantity') * F('emission_factor'), output_field=FloatField())
        ).values('year', 'month', 'company__name').annotate(
            total_co2=Sum('total_co2')
        ).order_by('year', 'month')

        # Prepare sorted lists of unique years and months
        years = sorted({emission['year'] for emission in annotated_qs})
        months = sorted({emission['month'] for emission in annotated_qs})

        # Prepare data dictionary for all companies, years, and months
        companies = {emission['company__name'] for emission in annotated_qs}
        data = {company: {year: {month: 0 for month in months} for year in years} for company in companies}

        # Populate data with actual emissions values
        for emission in annotated_qs:
            data[emission['company__name']][emission['year']][emission['month']] = emission['total_co2']

        # Serialize data structure for use in JavaScript
        context['years'] = years
        context['months'] = months
        context['data'] = json.dumps(data)
        context['chart_title'] = 'Fuel Emissions by Year and Month'

        return context


class NaturalGasEmissionsView(TemplateView):
    template_name = 'envdata/charts/display_charts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        annotated_qs = NaturalGas.objects.annotate(
            total_co2=Cast(F('quantity') * F('emission_factor'), output_field=FloatField())
        ).values('year', 'month', 'company__name').annotate(total_co2=Sum('total_co2')).order_by('year', 'month')

        years = sorted({emission['year'] for emission in annotated_qs})
        months = sorted({emission['month'] for emission in annotated_qs})

        # Prepare data dictionary for all companies, years, and months
        companies = {emission['company__name'] for emission in annotated_qs}
        data = {company: {year: {month: 0 for month in months} for year in years} for company in companies}

        # Populate data with actual emissions values
        for emission in annotated_qs:
            data[emission['company__name']][emission['year']][emission['month']] = emission['total_co2']

        # Serialize data structure for use in JavaScript
        context['years'] = years
        context['months'] = months
        context['data'] = json.dumps(data)
        context['chart_title'] = 'Natural Gas Emissions by Year and Month'

        return context


class Sf6EmissionsView(TemplateView):
    template_name = 'envdata/charts/display_charts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        annotated_qs = Sf6.objects.annotate(
            total_co2=Cast(F('quantity') * F('emission_factor'), output_field=FloatField())
        ).values('year', 'month', 'company__name').annotate(total_co2=Sum('total_co2')).order_by('year', 'month')

        years = sorted({emission['year'] for emission in annotated_qs})
        months = sorted({emission['month'] for emission in annotated_qs})

        # Prepare data dictionary for all companies, years, and months
        companies = {emission['company__name'] for emission in annotated_qs}
        data = {company: {year: {month: 0 for month in months} for year in years} for company in companies}

        # Populate data with actual emissions values
        for emission in annotated_qs:
            data[emission['company__name']][emission['year']][emission['month']] = emission['total_co2']

        # Serialize data structure for use in JavaScript
        context['years'] = years
        context['months'] = months
        context['data'] = json.dumps(data)
        context['chart_title'] = 'SF6 Emissions by Year and Month'

        return context


class RefrigerantEmissionsView(TemplateView):
    template_name = 'envdata/charts/display_charts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        annotated_qs = Refrigerant.objects.annotate(
            total_co2=Cast(F('quantity') * F('emission_factor'), output_field=FloatField())
        ).values('year','month', 'company__name').annotate(total_co2=Sum('total_co2')).order_by('year','month')

        years = sorted({emission['year'] for emission in annotated_qs})
        months = sorted({emission['month'] for emission in annotated_qs})

        # Prepare data dictionary for all companies, years, and months
        companies = {emission['company__name'] for emission in annotated_qs}
        data = {company: {year: {month: 0 for month in months} for year in years} for company in companies}

        # Populate data with actual emissions values
        for emission in annotated_qs:
            data[emission['company__name']][emission['year']][emission['month']] = emission['total_co2']

        # Serialize data structure for use in JavaScript
        context['years'] = years
        context['months'] = months
        context['data'] = json.dumps(data)
        context['chart_title'] = 'Refrigerant Emissions by Year'

        return context


class EnergyEmissionsView(TemplateView):
    template_name = 'envdata/charts/display_charts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        annotated_qs = Energy.objects.annotate(
            total_co2=Cast(F('quantity') * F('emission_factor'), output_field=FloatField())
        ).values('year', 'month','company__name').annotate(total_co2=Sum('total_co2')).order_by('year','month')

        years = sorted({emission['year'] for emission in annotated_qs})
        months = sorted({emission['month'] for emission in annotated_qs})

        # Prepare data dictionary for all companies, years, and months
        companies = {emission['company__name'] for emission in annotated_qs}
        data = {company: {year: {month: 0 for month in months} for year in years} for company in companies}

        # Populate data with actual emissions values
        for emission in annotated_qs:
            data[emission['company__name']][emission['year']][emission['month']] = emission['total_co2']

        # Serialize data structure for use in JavaScript
        context['years'] = years
        context['months'] = months
        context['data'] = json.dumps(data)
        context['chart_title'] = 'Energy Emissions by Year and Month'

        return context


class TravelEmissionsView(TemplateView):
    template_name = 'envdata/charts/display_charts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        annotated_qs = Travel.objects.annotate(
            total_co2=Cast(F('distance') * F('emission_factor'), output_field=FloatField())
        ).values('year', 'month', 'company__name').annotate(total_co2=Sum('total_co2')).order_by('year','month')

        years = sorted({emission['year'] for emission in annotated_qs})
        months = sorted({emission['month'] for emission in annotated_qs})

        # Prepare data dictionary for all companies, years, and months
        companies = {emission['company__name'] for emission in annotated_qs}
        data = {company: {year: {month: 0 for month in months} for year in years} for company in companies}

        # Populate data with actual emissions values
        for emission in annotated_qs:
            data[emission['company__name']][emission['year']][emission['month']] = emission['total_co2']

        # Serialize data structure for use in JavaScript
        context['years'] = years
        context['months'] = months
        context['data'] = json.dumps(data)
        context['chart_title'] = 'Travel Emissions by Year and Month'

        return context


class WasteEmissionsView(TemplateView):
    template_name = 'envdata/charts/display_charts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        annotated_qs = Waste.objects.annotate(
            total_co2=Cast(F('quantity_disposed') * F('emission_factor'), output_field=FloatField())
        ).values('year','month', 'company__name').annotate(total_co2=Sum('total_co2')).order_by('year','month')

        years = sorted({emission['year'] for emission in annotated_qs})
        months = sorted({emission['month'] for emission in annotated_qs})

        # Prepare data dictionary for all companies, years, and months
        companies = {emission['company__name'] for emission in annotated_qs}
        data = {company: {year: {month: 0 for month in months} for year in years} for company in companies}

        # Populate data with actual emissions values
        for emission in annotated_qs:
            data[emission['company__name']][emission['year']][emission['month']] = emission['total_co2']

        # Serialize data structure for use in JavaScript
        context['years'] = years
        context['months'] = months
        context['data'] = json.dumps(data)
        context['chart_title'] = 'Waste Emissions by Year and Month'

        return context
