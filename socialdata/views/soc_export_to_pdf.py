from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from envdata.mixins import CompanyContextMixin
from xhtml2pdf import pisa
from django.http import HttpResponse
from django.db.models import Sum, F
from django.template.loader import render_to_string
from .filters import HealthAndSafetyFilter
from socialdata.models import HealthAndSafety


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
