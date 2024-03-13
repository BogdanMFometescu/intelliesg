from django.views.generic import TemplateView
from envdata.mixins import CompanyContextMixin


class NavForms(TemplateView, CompanyContextMixin):
    template_name = 'nav_forms.html'



