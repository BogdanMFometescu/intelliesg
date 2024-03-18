from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from envdata.mixins import UpdateModeMixin, CompanyContextMixin
from envdata.models import Energy
from envdata.forms import EnergyForm
from django.contrib.auth.mixins import LoginRequiredMixin


class EnergyListView(LoginRequiredMixin, CompanyContextMixin, ListView):
    model = Energy
    template_name = 'envdata/scope_two_emission/energy_aq/energy-acquisitions.html'
    context_object_name = 'energy_acquisitions'


class EnergyDetailView(LoginRequiredMixin, CompanyContextMixin, DetailView):
    model = Energy
    template_name = 'envdata/scope_two_emission/energy_aq/energy-acquisition.html'
    context_object_name = 'energy_acquisition'


class EnergyCreateView(LoginRequiredMixin, CompanyContextMixin, CreateView):
    model = Energy
    form_class = EnergyForm
    template_name = 'envdata/scope_two_emission/energy_aq/form-energy-acquisition.html'
    success_url = reverse_lazy('energy_acquisitions')

    def form_valid(self, form):
        form.instance.owner = self.request.user.profile
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('energy_acquisitions')


class EnergyUpdateView(LoginRequiredMixin, UpdateModeMixin, CompanyContextMixin, UpdateView):
    model = Energy
    form_class = EnergyForm
    template_name = 'envdata/scope_two_emission/energy_aq/form-energy-acquisition.html'
    success_url = reverse_lazy('energy_acquisitions')


class EnergyDeleteView(LoginRequiredMixin, CompanyContextMixin, DeleteView):
    model = Energy
    template_name = 'envdata/delete-universal.html'
    success_url = reverse_lazy('energy_acquisitions')
