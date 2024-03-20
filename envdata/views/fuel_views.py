from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from envdata.mixins import UpdateModeMixin, CompanyContextMixin
from django.db.models import Sum,F
from envdata.models import Fuel
from envdata.forms import FuelForm
from .filters import FuelTypeFilter
from django.contrib.auth.mixins import LoginRequiredMixin
from django_filters.views import FilterView


class FuelListView(LoginRequiredMixin, CompanyContextMixin, FilterView):
    model = Fuel
    filterset_class = FuelTypeFilter
    template_name = 'envdata/scope_one_emission/fuel/fuel-emissions.html'
    context_object_name = 'fuel_emissions'

    def get_queryset(self):
        return super().get_queryset().order_by('year')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_co2'] = self.filterset.qs.annotate(
            co2e_for_fuel_emission=F('fuel_quantity') * F('emission_factor')
        ).aggregate(total_co2e=Sum('co2e_for_fuel_emission'))['total_co2e'] or 0
        return context


class FuelDetailView(LoginRequiredMixin, CompanyContextMixin, DetailView):
    model = Fuel
    template_name = 'envdata/scope_one_emission/fuel/fuel-emission.html'
    context_object_name = 'fuel_emission'


class FuelCreateView(LoginRequiredMixin, CompanyContextMixin, CreateView):
    model = Fuel
    form_class = FuelForm
    template_name = 'envdata/scope_one_emission/fuel/form-fuel.html'
    success_url = reverse_lazy('fuel_emissions')

    def form_valid(self, form):
        form.instance.owner = self.request.user.profile
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('fuel_emissions')


class FuelUpdateView(LoginRequiredMixin, UpdateModeMixin, CompanyContextMixin, UpdateView):
    model = Fuel
    form_class = FuelForm
    template_name = 'envdata/scope_one_emission/fuel/form-fuel.html'
    success_url = reverse_lazy('fuel_emissions')


class FuelDeleteView(LoginRequiredMixin, CompanyContextMixin, DeleteView):
    model = Fuel
    template_name = 'envdata/delete-universal.html'
    success_url = reverse_lazy('fuel_emissions')
