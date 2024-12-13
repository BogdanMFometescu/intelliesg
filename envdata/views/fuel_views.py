from django.urls import reverse_lazy
from django.views.generic import (DetailView, CreateView, UpdateView, DeleteView)
from common.mixins import UpdateModeMixin, CompanyContextMixin
from django.db.models import Sum, F
from envdata.models import Fuel
from envdata.forms import FuelForm
from .filters import FuelTypeFilter
from django.contrib.auth.mixins import LoginRequiredMixin
from django_filters.views import FilterView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class FuelListView(LoginRequiredMixin, CompanyContextMixin, FilterView):
    model = Fuel
    filterset_class = FuelTypeFilter
    template_name = 'envdata/scope_one_emission/fuel/fuel-emissions.html'
    context_object_name = 'fuel_emissions'
    paginate_by = 50

    def get_queryset(self):
        if self.request.user.is_staff:
            return super().get_queryset()
        return Fuel.objects.filter(profile__user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        filtered_qs = self.filterset.qs.annotate(
            co2e_for_fuel_emission=F('quantity') * F('emission_factor')
        ).aggregate(total_co2e=Sum('co2e_for_fuel_emission'))['total_co2e'] or 0

        # Pagination
        paginator = Paginator(self.filterset.qs, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            fuel_emissions = paginator.page(page)
        except PageNotAnInteger:
            fuel_emissions = paginator.page(1)
        except EmptyPage:
            fuel_emissions = paginator.page(paginator.num_pages)

        context['fuel_emissions'] = fuel_emissions
        context['total_co2'] = filtered_qs
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

    def get_form_kwargs(self):
        kwargs = super(FuelCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user  # Pass the user to the form
        return kwargs

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('fuel_emissions')


class FuelUpdateView(LoginRequiredMixin, UpdateModeMixin, CompanyContextMixin, UpdateView):
    model = Fuel
    form_class = FuelForm
    template_name = 'envdata/scope_one_emission/fuel/form-fuel.html'
    success_url = reverse_lazy('fuel_emissions')

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile  # Ensure the profile is set to the current user's profile
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(FuelUpdateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user  # Pass the user to the form
        return kwargs


class FuelDeleteView(LoginRequiredMixin, CompanyContextMixin, DeleteView):
    model = Fuel
    template_name = 'envdata/delete-universal.html'
    success_url = reverse_lazy('fuel_emissions')
