from django.views.generic import TemplateView
from envdata.mixins import CompanyContextMixin
from django.contrib.auth.mixins import LoginRequiredMixin


class NavFormPillars(LoginRequiredMixin, TemplateView, CompanyContextMixin):
    template_name = 'esgmanager/esg_nav_forms/nav-forms-pillars.html'


class NavFormActionPlan(LoginRequiredMixin, TemplateView, CompanyContextMixin):
    template_name = 'esgmanager/esg_nav_forms/nav-forms-action-plan.html'


class NavFormObjectives(LoginRequiredMixin, TemplateView, CompanyContextMixin):
    template_name = 'esgmanager/esg_nav_forms/nav-forms-objectives.html'


class NavFormActions(LoginRequiredMixin, TemplateView, CompanyContextMixin):
    template_name = 'esgmanager/esg_nav_forms/nav-forms-actions.html'


class NavFormsRisks(LoginRequiredMixin, TemplateView, CompanyContextMixin):
    template_name = 'esgmanager/esg_nav_forms/nav-forms-risks.html'


class NavListRisks(LoginRequiredMixin,TemplateView,CompanyContextMixin):
    template_name = 'esgmanager/risks/esg-risks-list.html'

