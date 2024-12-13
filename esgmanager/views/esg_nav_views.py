from django.views.generic import TemplateView
from common.mixins import CompanyContextMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from esgmanager.models import EnvironmentalRisk, GovernanceRisks, SocialRisk, ClimateChangeRisk


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


class NavListRisks(LoginRequiredMixin, TemplateView, CompanyContextMixin):
    template_name = 'esgmanager/risks/esg-risks-list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['risk_count'] = EnvironmentalRisk.objects.count()
        context['gov_risk_count'] = GovernanceRisks.objects.count()
        context['social_risk_count'] = SocialRisk.objects.count()
        context['climate_risk_count'] = ClimateChangeRisk.objects.count()
        return context
