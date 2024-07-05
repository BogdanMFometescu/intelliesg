from django.views.generic import TemplateView
from envdata.mixins import CompanyContextMixin
from django.contrib.auth.mixins import LoginRequiredMixin


class NavFormsHealthAndSafety(LoginRequiredMixin, TemplateView, CompanyContextMixin):
    template_name = 'socialdata/soc_nav_forms/nav-forms-health-and-safety.html'



class NavFormsEmployees(LoginRequiredMixin, TemplateView, CompanyContextMixin):
    template_name = 'socialdata/soc_nav_forms/nav-forms-employees.html'
