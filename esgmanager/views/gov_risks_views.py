from esgmanager.models import GovernanceRisks
from esgmanager.forms import GovernanceRisksForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from envdata.mixins import CompanyContextMixin, UpdateModeMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class GovernanceRiskListView(LoginRequiredMixin, CompanyContextMixin, ListView):
    model = GovernanceRisks
    template_name = 'esgmanager/risks/governance/gov-risks.html'
    context_object_name = 'governance_risks'


class GovernanceRiskDetailView(LoginRequiredMixin, CompanyContextMixin, DetailView):
    model = GovernanceRisks
    template_name = 'esgmanager/risks/governance/gov-risk.html'
    context_object_name = 'governance_risk'


class GovernanceRiskCreateView(LoginRequiredMixin, CompanyContextMixin, CreateView):
    form_class = GovernanceRisksForm
    template_name = 'esgmanager/risks/governance/form-gov-risk.html'
    success_url = reverse_lazy('governance_risks')

    def form_valid(self, form):
        form.instance.owner = self.request.user.profile
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('governance_risks')


class GovernanceRiskUpdateView(LoginRequiredMixin, CompanyContextMixin, UpdateView, UpdateModeMixin):
    model = GovernanceRisks
    form_class = GovernanceRisksForm
    template_name = 'esgmanager/risks/governance/form-gov-risk.html'
    success_url = reverse_lazy('governance_risks')


class GovernanceRiskDeleteView(LoginRequiredMixin, CompanyContextMixin, DeleteView):
    model = GovernanceRisks
    template_name = 'envdata/delete-universal.html'
    success_url = reverse_lazy('governance_risks')