from django.db.models import F, FloatField,Sum
from django.db.models.functions import Cast
from django.views.generic import TemplateView

from envdata.models import Fuel


class FuelEmissionsView(TemplateView):
    template_name = 'envdata/charts/emissions_chart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Annotate the queryset with a calculated CO2 emissions field
        # This is a simplified example; adjust the calculation as needed
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
