from companies.models import Company
from django.views.generic.base import ContextMixin

class UpdateModeMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update_mode'] = True
        return context


class CompanyContextMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['company'] = Company.objects.first()
        return context



