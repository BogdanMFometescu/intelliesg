from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from envdata.mixins import CompanyContextMixin
from .filters import FuelTypeFilter
from envdata.models import Fuel
from xhtml2pdf import pisa
from django.http import HttpResponse
from django.db.models import Sum, F
from django.template.loader import render_to_string


class FuelExportPdfView(LoginRequiredMixin, CompanyContextMixin, View):
    def get(self, request, *args, **kwargs):
        filter_set = FuelTypeFilter(request.GET, queryset=Fuel.objects.all().order_by('year'))
        fuel_filtered = filter_set.qs

        total_co2 = fuel_filtered.annotate(
            co2e_for_fuel_emission=F('fuel_quantity') * F('emission_factor')
        ).aggregate(total_co2e=Sum('co2e_for_fuel_emission'))['total_co2e'] or 0

        html_string = render_to_string('envdata/export_to_pdf/fuel_report.html', {'fuels': fuel_filtered,
                                                                                  'total_co2': total_co2})

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment;filename="fuel_report.pdf"'

        pisa_status = pisa.CreatePDF(html_string, dest=response)

        if pisa_status.err:
            return HttpResponse('We had some errors. Please try again' + html_string + '</pre>')
        return response
