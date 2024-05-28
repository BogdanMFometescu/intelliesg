from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from envdata.mixins import CompanyContextMixin
from .filters import FuelTypeFilter, Sf6TypeFilter, RefrigerantTypeFilter, NaturalGasTypeFilter, EnergyTypeFilter, \
    WasteTypeFilter, TravelTypeFilter, TaxonomyTurnoverFilter, TaxonomyOpeExFilter
from envdata.models import Fuel, Sf6, Refrigerant, NaturalGas, Energy, Waste, Travel, TaxonomyTurnover, TaxonomyOpEx
from xhtml2pdf import pisa
from django.http import HttpResponse
from django.db.models import Sum, F
from django.template.loader import render_to_string


class FuelExportPdfView(LoginRequiredMixin, View):
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


class Sf6ExportPdfView(LoginRequiredMixin, CompanyContextMixin, View):
    def get(self, request, *args, **kwargs):
        filter_set = Sf6TypeFilter(request.GET, queryset=Sf6.objects.all().order_by('year'))
        sf6_filtered = filter_set.qs

        total_co2 = sf6_filtered.annotate(co2_for_sf6_emission=F('sf6_quantity') * F('emission_factor')).aggregate(
            total_co2=Sum('co2_for_sf6_emission'))['total_co2'] or 0

        html_string = render_to_string('envdata/export_to_pdf/sf6_report.html', {'sf6_filtered': sf6_filtered,
                                                                                 'total_co2': total_co2})

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment;filename=sf6_report.pdf'
        pisa_status = pisa.CreatePDF(html_string, dest=response)

        if pisa_status.err:
            return HttpResponse('We had some errors. Please try again' + html_string + '</pre>')
        return response


class RefrigerantPdfView(LoginRequiredMixin, CompanyContextMixin, View):
    def get(self, request, *args, **kwargs):
        filter_set = RefrigerantTypeFilter(request.GET, queryset=Refrigerant.objects.all().order_by('year'))
        filtered_refrigerants = filter_set.qs

        total_co2 = \
            filtered_refrigerants.annotate(
                co2_for_refrigerant=F('refrigerant_quantity') * F('emission_factor')).aggregate(
                total_co2=Sum('co2_for_refrigerant'))['total_co2'] or 0

        html_string = render_to_string('envdata/export_to_pdf/refrigerant_report.html',
                                       {'refrigerants': filtered_refrigerants,
                                        'total_co2': total_co2})

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment;filename=refrigerant_report.pdf'

        pisa_status = pisa.CreatePDF(html_string, dest=response)
        if pisa_status.err:
            return HttpResponse('We had some errors. Please try again' + html_string + '</pre>')
        return response


class NaturalGasPdfView(LoginRequiredMixin, CompanyContextMixin, View):
    def get(self, request, *args, **kwargs):
        filter_set = NaturalGasTypeFilter(request.GET, queryset=NaturalGas.objects.all().order_by('year'))
        filtered_gas = filter_set.qs

        total_co2 = \
            filtered_gas.annotate(
                co2_for_gas=F('gas_quantity') * F('emission_factor')).aggregate(
                total_co2=Sum('co2_for_gas'))['total_co2'] or 0

        html_string = render_to_string('envdata/export_to_pdf/gas_report.html',
                                       {'gas': filtered_gas,
                                        'total_co2': total_co2})

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment;filename=gas_report.pdf'

        pisa_status = pisa.CreatePDF(html_string, dest=response)
        if pisa_status.err:
            return HttpResponse('We had some errors. Please try again' + html_string + '</pre>')
        return response


class EnergyPdfView(LoginRequiredMixin, CompanyContextMixin, View):
    def get(self, request, *args, **kwargs):
        filter_set = EnergyTypeFilter(request.GET, queryset=Energy.objects.all().order_by('year'))
        filtered_energy = filter_set.qs

        total_co2 = \
            filtered_energy.annotate(
                co2_for_energy=F('energy_quantity') * F('emission_factor')).aggregate(
                total_co2=Sum('co2_for_energy'))['total_co2'] or 0

        html_string = render_to_string('envdata/export_to_pdf/energy_report.html',
                                       {'energy': filtered_energy,
                                        'total_co2': total_co2})

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment;filename=energy_report.pdf'

        pisa_status = pisa.CreatePDF(html_string, dest=response)
        if pisa_status.err:
            return HttpResponse('We had some errors. Please try again' + html_string + '</pre>')
        return response


class WastePdfView(LoginRequiredMixin, CompanyContextMixin, View):
    def get(self, request, *args, **kwargs):
        filter_set = WasteTypeFilter(request.GET, queryset=Waste.objects.all().order_by('year'))
        filtered_waste = filter_set.qs

        total_co2 = \
            filtered_waste.annotate(
                co2_for_waste=F('quantity_disposed') * F('emission_factor')).aggregate(
                total_co2=Sum('co2_for_waste'))['total_co2'] or 0

        html_string = render_to_string('envdata/export_to_pdf/waste_report.html',
                                       {'waste': filtered_waste,
                                        'total_co2': total_co2})

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment;filename=waste_report.pdf'

        pisa_status = pisa.CreatePDF(html_string, dest=response)
        if pisa_status.err:
            return HttpResponse('We had some errors. Please try again' + html_string + '</pre>')
        return response


class TravelPdfView(LoginRequiredMixin, CompanyContextMixin, View):
    def get(self, request, *args, **kwargs):
        filter_set = TravelTypeFilter(request.GET, queryset=Travel.objects.all().order_by('year'))
        filtered_travel = filter_set.qs

        total_co2 = \
            filtered_travel.annotate(
                co2_for_travel=F('distance') * F('emission_factor')).aggregate(
                total_co2=Sum('co2_for_travel'))['total_co2'] or 0

        html_string = render_to_string('envdata/export_to_pdf/travel_report.html',
                                       {'travel': filtered_travel,
                                        'total_co2': total_co2})

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment;filename=travel_report.pdf'

        pisa_status = pisa.CreatePDF(html_string, dest=response)
        if pisa_status.err:
            return HttpResponse('We had some errors. Please try again' + html_string + '</pre>')
        return response


class TaxonomyTurnoverPdfView(LoginRequiredMixin, CompanyContextMixin, View):
    def get(self, request, *args, **kwargs):
        filter_set = TaxonomyTurnoverFilter(request.GET, queryset=TaxonomyTurnover.objects.all())
        filtered_turnover = filter_set.qs
        total_turnover = \
            filtered_turnover.annotate(
                total_eligible_turnover=F('turnover_eligible') + F('turnover_aligned')).aggregate(
                total_eligible=Sum('total_eligible_turnover'))['total_eligible'] or 0
        html_string = render_to_string('envdata/export_to_pdf/turnover_report.html',
                                       {'taxonomy_turnover': filtered_turnover,
                                        'total_turnover': total_turnover})
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment;filename=turnover_report.pdf'

        pisa_status = pisa.CreatePDF(html_string, dest=response)
        if pisa_status.err:
            return HttpResponse('We had some errors. Please try again' + html_string + '</pre>')
        return response


class TaxonomyOpExPdfView(LoginRequiredMixin, CompanyContextMixin, View):
    def get(self, request, *args, **kwargs):
        filter_set = TaxonomyOpeExFilter(request.GET, queryset=TaxonomyOpEx.objects.all())
        filtered_opex = filter_set.qs
        total_opex = \
            filtered_opex.annotate(
                total_eligible_opex=F('opex_eligible') + F('opex_aligned')).aggregate(
                total_eligible=Sum('total_eligible_opex'))['total_eligible'] or 0
        html_string = render_to_string('envdata/export_to_pdf/opex_report.html',
                                       {'taxonomy_opex': filtered_opex,
                                        'total_opex': total_opex})
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment;filename=opex_report.pdf'

        pisa_status = pisa.CreatePDF(html_string, dest=response)
        if pisa_status.err:
            return HttpResponse('We had some errors. Please try again' + html_string + '</pre>')
        return response
