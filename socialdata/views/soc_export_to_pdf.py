from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from common.mixins import CompanyContextMixin
from xhtml2pdf import pisa
from django.http import HttpResponse
from django.db.models import Sum, F
from django.template.loader import render_to_string
from .filters import HealthAndSafetyFilter, EmployeeContractsFilter, NewEmployeeByAgeFilter
from socialdata.models import HealthAndSafety, EmployeeByContracts, NewEmployeeByAge


class HealthAndSafetyPdfView(LoginRequiredMixin, CompanyContextMixin, View):
    def get(self, request, *args, **kwargs):
        filter_set = HealthAndSafetyFilter(request.GET, queryset=HealthAndSafety.objects.all())
        filtered_hs = filter_set.qs
        total_hours = \
            filtered_hs.annotate(total_wh=F('total_working_hours')).aggregate(
                total_hours=Sum('total_wh'))['total_hours'] or 0

        total_hours_ep = \
            filtered_hs.annotate(total_wh_ep=F('ep_total_working_hours')).aggregate(total_hours_ep=Sum('total_wh_ep'))[
                'total_hours_ep'] or 0

        total_training_hours = filtered_hs.annotate(total_training=F('total_training_hours')).aggregate(
            total=Sum('total_training'))['total'] or 0

        html_string = render_to_string('socialdata/export_to_pdf/health-and-safety-report.html',
                                       {'total_hs_hours': filtered_hs,
                                        'total_hs_hours_ep': total_hours_ep,
                                        'total_training_hours': total_training_hours,
                                        'total_hours': total_hours})
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment;filename=health_and_safety_report.pdf'

        pisa_status = pisa.CreatePDF(html_string, dest=response)
        if pisa_status.err:
            return HttpResponse('We had some errors. Please try again' + html_string + '</pre>')
        return response


class EmployeeContractsPdfView(LoginRequiredMixin, CompanyContextMixin, View):
    def get(self, request, *args, **kwargs):
        filter_set = EmployeeContractsFilter(request.GET, queryset=EmployeeByContracts.objects.all())
        filtered_hs = filter_set.qs
        filtered_full_time_contracts = \
            filtered_hs.annotate(total_contracts=F('full_time_women') + F('full_time_men')).aggregate(
                total_contract_full=Sum('total_contracts'))['total_contract_full'] or 0

        filtered_fixed_term_contracts = filtered_hs.annotate(
            total_contracts_ft=F('fixed_term_contract_women') + F('fixed_term_contract_men')).aggregate(
            total_contract_fixed=Sum('total_contracts_ft'))['total_contract_fixed'] or 0

        filtered_part_time_contracts = filtered_hs.annotate(
            total_contracts_pt=F('part_time_women') + F('part_time_men')).aggregate(
            total_contract_part=Sum('total_contracts_pt'))['total_contract_part'] or 0

        filtered_total_contracts = filtered_hs.annotate(
            total_company_contracts=F('part_time_women') + F('part_time_men') + F('full_time_women') + F(
                'full_time_men') + F('fixed_term_contract_women') + F('fixed_term_contract_men')).aggregate(
            total=Sum('total_company_contracts'))['total'] or 0

        html_string = render_to_string('socialdata/export_to_pdf/contracts-report.html',
                                       {'total_company_contracts': filtered_hs,
                                        'total_full_time': filtered_full_time_contracts,
                                        'total_fixed_term': filtered_fixed_term_contracts,
                                        'total_part_time': filtered_part_time_contracts,
                                        'total_contracts': filtered_total_contracts})
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment;filename=employee_contracts_report.pdf'

        pisa_status = pisa.CreatePDF(html_string, dest=response)
        if pisa_status.err:
            return HttpResponse('We had some errors. Please try again' + html_string + '</pre>')
        return response


class EmployeeAgePdfView(LoginRequiredMixin, CompanyContextMixin, View):
    def get(self, request, *args, **kwargs):
        filter_set = NewEmployeeByAgeFilter(request.GET, queryset=NewEmployeeByAge.objects.all())
        filtered_hs = filter_set.qs
        filtered_under_30 = \
            filtered_hs.annotate(total_under_30=F('men_under_30') + F('women_under_30')).aggregate(
                total_emp_under_30=Sum('total_under_30'))['total_emp_under_30'] or 0

        filtered_between_30_and_50 = filtered_hs.annotate(
            total_between_30_and_50=F('men_between_30_and_50') + F('women_between_30_and_50')).aggregate(
            total_30_and_50=Sum('total_between_30_and_50'))['total_30_and_50'] or 0

        filtered_over_50 = filtered_hs.annotate(total_over_50=F('men_over_50') + F('women_over_50')).aggregate(
            total_over=Sum('total_over_50'))['total_over'] or 0

        filtered_total_employees_by_age = filtered_hs.annotate(
            total_employees=F('men_under_30') + F('women_under_30') + F('men_between_30_and_50') + F(
                'women_between_30_and_50') + F('men_over_50') + F('women_over_50')).aggregate(
            total=Sum('total_employees'))['total'] or 0

        html_string = render_to_string('socialdata/export_to_pdf/employees-by-age-report.html',
                                       {'total_age_filtered': filtered_hs,
                                        'total_under_30': filtered_under_30,
                                        'total_between_30_and_50': filtered_between_30_and_50,
                                        'total_over_50': filtered_over_50,
                                        'total_age_sum': filtered_total_employees_by_age})
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment;filename=age_report.pdf'

        pisa_status = pisa.CreatePDF(html_string, dest=response)
        if pisa_status.err:
            return HttpResponse('We had some errors. Please try again' + html_string + '</pre>')
        return response
