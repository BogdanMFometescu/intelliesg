from esgmanager.models import EnvironmentalRisk
from esgmanager.forms import EnvironmentalRisksForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from common.mixins import CompanyContextMixin, UpdateModeMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class EnvRiskListView(LoginRequiredMixin, CompanyContextMixin, ListView):
    model = EnvironmentalRisk
    template_name = 'esgmanager/risks/environmental/env-risks.html'
    context_object_name = 'env_risks'


class EnvRiskDetailView(LoginRequiredMixin, CompanyContextMixin, DetailView):
    model = EnvironmentalRisk
    template_name = 'esgmanager/risks/environmental/env-risk.html'
    context_object_name = 'env_risk'


class EnvRiskCreateView(LoginRequiredMixin, CompanyContextMixin, CreateView):
    form_class = EnvironmentalRisksForm
    template_name = 'esgmanager/risks/environmental/form-env-risk.html'
    success_url = reverse_lazy('env_risks')

    def form_valid(self, form):
        form.instance.owner = self.request.user.profile
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('env_risks')


class EnvRiskUpdateView(LoginRequiredMixin, CompanyContextMixin, UpdateView, UpdateModeMixin):
    model = EnvironmentalRisk
    form_class = EnvironmentalRisksForm
    template_name = 'esgmanager/risks/environmental/form-env-risk.html'
    success_url = reverse_lazy('env_risks')


class EnvRiskDeleteView(LoginRequiredMixin, CompanyContextMixin, DeleteView):
    model = EnvironmentalRisk
    template_name = 'envdata/delete-universal.html'
    success_url = reverse_lazy('env_risks')
