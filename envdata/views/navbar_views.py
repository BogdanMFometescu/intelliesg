from django.views.generic import TemplateView
from envdata.mixins import CompanyContextMixin
from django.contrib.auth.mixins import LoginRequiredMixin


class NavForms(LoginRequiredMixin, TemplateView, CompanyContextMixin):
    template_name = 'nav_forms.html'
