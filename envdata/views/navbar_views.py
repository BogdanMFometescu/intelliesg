from django.views.generic import TemplateView
from envdata.mixins import CompanyContextMixin
from django.contrib.auth.mixins import LoginRequiredMixin


class NavFormsCompany(LoginRequiredMixin, TemplateView, CompanyContextMixin):
    template_name = 'envdata/env_nav_forms/nav-forms-company.html'


class NavFormsTargets(LoginRequiredMixin, TemplateView, CompanyContextMixin):
    template_name = 'envdata/env_nav_forms/nav-forms-targets.html'


class NavFormsEmissions(LoginRequiredMixin, TemplateView, CompanyContextMixin):
    template_name = 'envdata/env_nav_forms/nav-forms-emissions.html'


class NavFormsTaxonomy(LoginRequiredMixin, TemplateView, CompanyContextMixin):
    template_name = 'envdata/env_nav_forms/nav-forms-taxonomy.html'


