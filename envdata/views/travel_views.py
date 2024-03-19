from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from envdata.mixins import UpdateModeMixin, CompanyContextMixin
from envdata.models import Travel
from envdata.forms import TravelForm
from .filters import TravelTypeFilter
from django.contrib.auth.mixins import LoginRequiredMixin
from django_filters.views import FilterView
from django.db.models import Sum, F


class TravelListView(LoginRequiredMixin, CompanyContextMixin, FilterView):
    model = Travel
    filterset_class = TravelTypeFilter
    template_name = 'envdata/scope_one_emission/travel/travels.html'
    context_object_name = 'travels'

    def get_queryset(self):
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_co2'] = \
            self.filterset.qs.annotate(co2_for_travel=F('distance') * F('emission_factor')).aggregate(
                total_co2=Sum('co2_for_travel'))['total_co2'] or 0
        return context


class TravelDetailView(LoginRequiredMixin, CompanyContextMixin, DetailView):
    model = Travel
    template_name = 'envdata/scope_one_emission/travel/travel.html'
    context_object_name = 'travel'


class TravelCreateView(LoginRequiredMixin, CompanyContextMixin, CreateView):
    model = Travel
    form_class = TravelForm
    template_name = 'envdata/scope_one_emission/travel/form-travel.html'
    success_url = reverse_lazy('travels')

    def form_valid(self, form):
        form.instance.owner = self.request.user.profile
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('travels')


class TravelUpdateView(LoginRequiredMixin, UpdateModeMixin, CompanyContextMixin, UpdateView):
    model = Travel
    form_class = TravelForm
    template_name = 'envdata/scope_one_emission/travel/form-travel.html'
    success_url = reverse_lazy('travels')


class TravelDeleteView(LoginRequiredMixin, CompanyContextMixin, DeleteView):
    model = Travel
    template_name = 'envdata/delete-universal.html'
    success_url = reverse_lazy('travels')
