from django.urls import reverse_lazy
from django.views.generic import (DetailView, CreateView, UpdateView, DeleteView)
from envdata.mixins import UpdateModeMixin, CompanyContextMixin
from envdata.models import Energy
from envdata.forms import EnergyForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django_filters.views import FilterView
from .filters import EnergyTypeFilter
from django.db.models import Sum, F
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class EnergyListView(LoginRequiredMixin, CompanyContextMixin, FilterView):
    model = Energy
    filterset_class = EnergyTypeFilter
    template_name = 'envdata/scope_two_emission/energy_aq/energy-acquisitions.html'
    context_object_name = 'energy_acquisitions'
    paginate_by = 50

    def get_queryset(self):
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        filtered_qs = \
            self.filterset.qs.annotate(co2_for_energy_emissions=F('energy_quantity') * F('emission_factor')).aggregate(
                total_co2=Sum('co2_for_energy_emissions'))['total_co2'] or 0

        paginator = Paginator(self.filterset.qs, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            energy_acquisitions = paginator.page(page)
        except PageNotAnInteger:
            energy_acquisitions = paginator.page(1)
        except EmptyPage:
            energy_acquisitions = paginator.page(paginator.num_pages)

        context['energy_acquisitions'] = energy_acquisitions
        context['total_co2'] = filtered_qs

        return context


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
