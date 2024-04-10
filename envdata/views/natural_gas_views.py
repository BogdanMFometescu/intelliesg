from django.views.generic import (DetailView, CreateView, UpdateView, DeleteView)
from django_filters.views import FilterView
from django.urls import reverse_lazy
from envdata.models import NaturalGas
from envdata.forms import NaturalGasForm
from .filters import NaturalGasTypeFilter
from envdata.mixins import CompanyContextMixin, UpdateModeMixin
from django.db.models import Sum, F
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class NaturalGasListView(CompanyContextMixin, LoginRequiredMixin, FilterView):
    model = NaturalGas
    filterset_class = NaturalGasTypeFilter
    template_name = 'envdata/scope_one_emission/gas/natural_gas_emissions.html'
    context_object_name = 'gas_emissions'
    paginate_by = 50

    def get_queryset(self):
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        filtered_qs = \
            self.filterset.qs.annotate(co2_for_gas_emissions=F('gas_quantity') * F('emission_factor')).aggregate(
                total_co2=Sum('co2_for_gas_emissions'))['total_co2'] or 0

        paginator = Paginator(self.filterset.qs, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            gas_emissions = paginator.page(page)
        except PageNotAnInteger:
            gas_emissions = paginator.page(1)
        except EmptyPage:
            gas_emissions = paginator.page(paginator.num_pages)

        context['gas_emissions'] = gas_emissions
        context['total_co2'] = filtered_qs
        return context


class NaturalGasDetailView(CompanyContextMixin, LoginRequiredMixin, DetailView):
    model = NaturalGas
    template_name = 'envdata/scope_one_emission/gas/natural_gas_emission.html'
    context_object_name = 'gas_emission'


class NaturalGasCreateView(CompanyContextMixin, LoginRequiredMixin, CreateView):
    model = NaturalGas
    form_class = NaturalGasForm
    template_name = 'envdata/scope_one_emission/gas/form-natural-gas.html'
    success_url = reverse_lazy('gas_emissions')

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('gas_emissions')


class NaturalGasUpdateView(CompanyContextMixin, LoginRequiredMixin, UpdateView, UpdateModeMixin):
    model = NaturalGas
    template_name = 'envdata/scope_one_emission/gas/form-natural-gas.html'
    form_class = NaturalGasForm
    success_url = reverse_lazy('gas_emissions')


class NaturalGasDeleteView(CompanyContextMixin, LoginRequiredMixin, DeleteView):
    model = NaturalGas
    template_name = 'envdata/delete-universal.html'
    success_url = reverse_lazy('gas_emissions')
