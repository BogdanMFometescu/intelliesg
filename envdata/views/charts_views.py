from django.views.generic import DetailView
from envdata.models import Company, Fuel
from django.db.models import Sum, F


class FuelEmissionsDetailView(DetailView):
    model = Company
    template_name = 'envdata/charts/fuel_chart.html'
    context_object_name = 'company'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        company_id = self.object.id

        emissions_data = Fuel.objects.filter(company_id=company_id) \
            .values('year') \
            .annotate(total_co2=Sum(F('fuel_quantity') * F('emission_factor'))) \
            .order_by('year')

        years = [data['year'] for data in emissions_data]
        emissions = [data['total_co2'] for data in emissions_data]

        context['years'] = years
        context['emissions'] = emissions
        return context
