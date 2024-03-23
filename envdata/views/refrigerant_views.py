from django.urls import reverse_lazy
from django.views.generic import (DetailView, CreateView, UpdateView, DeleteView)
from envdata.mixins import UpdateModeMixin, CompanyContextMixin
from envdata.models import Refrigerant
from envdata.forms import RefrigerantForm
from .filters import RefrigerantTypeFilter
from django.contrib.auth.mixins import LoginRequiredMixin
from django_filters.views import FilterView
from django.db.models import Sum, F
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class RefrigerantView(LoginRequiredMixin, CompanyContextMixin, FilterView):
    model = Refrigerant
    filterset_class = RefrigerantTypeFilter
    template_name = 'envdata/scope_one_emission/refrigerant/refrigerant-emissions.html'
    context_object_name = 'refrigerants_emissions'
    paginate_by = 5

    def get_queryset(self):
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        filtered_qs = \
            self.filterset.qs.annotate(co2_for_refrigerant=F('refrigerant_quantity') * F('emission_factor')).aggregate(
                total_co2=Sum('co2_for_refrigerant'))['total_co2'] or 0

        paginator = Paginator(self.filterset.qs, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            refrigerants = paginator.page(page)
        except PageNotAnInteger:
            refrigerants = paginator.page(1)
        except EmptyPage:
            refrigerants = paginator.page(paginator.num_pages)

        context['refrigerants'] = refrigerants
        context['total_co2'] = filtered_qs

        return context


class RefrigerantDetailView(LoginRequiredMixin, CompanyContextMixin, DetailView):
    model = Refrigerant
    template_name = 'envdata/scope_one_emission/refrigerant/refrigerant-emission.html'
    context_object_name = 'refrigerant_emission'


class RefrigerantCreateView(LoginRequiredMixin, CompanyContextMixin, CreateView):
    model = Refrigerant
    form_class = RefrigerantForm
    template_name = 'envdata/scope_one_emission/refrigerant/form-refrigerant.html'
    success_url = reverse_lazy('refrigerant_emissions')

    def form_valid(self, form):
        form.instance.owner = self.request.user.profile
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('refrigerant_emissions')


class RefrigerantUpdateView(LoginRequiredMixin, UpdateModeMixin, CompanyContextMixin, UpdateView):
    model = Refrigerant
    form_class = RefrigerantForm
    template_name = 'envdata/scope_one_emission/refrigerant/form-refrigerant.html'
    success_url = reverse_lazy('refrigerant_emissions')


class RefrigerantDeleteView(LoginRequiredMixin, CompanyContextMixin, DeleteView):
    model = Refrigerant
    template_name = 'envdata/delete-universal.html'
    success_url = reverse_lazy('refrigerant_emissions')
