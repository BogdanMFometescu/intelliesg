from esgmanager.models import ClimateChangeRisk
from esgmanager.forms import ClimateChangeRisksForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from envdata.mixins import CompanyContextMixin, UpdateModeMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class ClimateRiskListView(LoginRequiredMixin, CompanyContextMixin, ListView):
    model = ClimateChangeRisk
    template_name = 'esgmanager/risks/climate_change/cc-risks.html'
    context_object_name = 'climate_risks'


class ClimateRiskDetailView(LoginRequiredMixin, CompanyContextMixin, DetailView):
    model = ClimateChangeRisk
    template_name = 'esgmanager/risks/climate_change/cc-risk.html'
    context_object_name = 'climate_risk'


class ClimateRiskCreateView(LoginRequiredMixin, CompanyContextMixin, CreateView):
    form_class = ClimateChangeRisksForm
    template_name = 'esgmanager/risks/climate_change/form-cc-risk.html'
    success_url = reverse_lazy('climate_risks')

    def form_valid(self, form):
        form.instance.owner = self.request.user.profile
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('climate_risks')


class ClimateRiskUpdateView(LoginRequiredMixin, CompanyContextMixin, UpdateView, UpdateModeMixin):
    model = ClimateChangeRisk
    form_class = ClimateChangeRisksForm
    template_name = 'esgmanager/risks/climate_change/form-cc-risk.html'
    success_url = reverse_lazy('climate_risks')


class ClimateRiskDeleteView(LoginRequiredMixin, CompanyContextMixin, DeleteView):
    model = ClimateChangeRisk
    template_name = 'envdata/delete-universal.html'
    success_url = reverse_lazy('climate_risks')
