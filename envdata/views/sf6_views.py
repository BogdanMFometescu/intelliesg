from django.urls import reverse_lazy
from django.views.generic import (DetailView, CreateView, UpdateView, DeleteView)
from common.mixins import UpdateModeMixin, CompanyContextMixin
from envdata.models import Sf6
from envdata.forms import Sf6Form
from .filters import Sf6TypeFilter
from django.contrib.auth.mixins import LoginRequiredMixin
from django_filters.views import FilterView
from django.db.models import Sum, F
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class Sf6ListView(LoginRequiredMixin, CompanyContextMixin, FilterView):
    model = Sf6
    filterset_class = Sf6TypeFilter
    template_name = 'envdata/scope_one_emission/sf6/sf6-emissions.html'
    context_object_name = 'sf6_emissions'
    paginate_by = 50

    def get_queryset(self):
        if self.request.user.is_staff:
            return super().get_queryset()
        return Sf6.objects.filter(profile__user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        filtered_qs = \
            self.filterset.qs.annotate(co2_for_sf6=F('quantity') * F('emission_factor')).aggregate(
                total_co2=(Sum('co2_for_sf6')))['total_co2'] or 0
        paginator = Paginator(self.filterset.qs, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            sf6_emissions = paginator.page(page)
        except PageNotAnInteger:
            sf6_emissions = paginator.page(1)
        except EmptyPage:
            sf6_emissions = paginator.page(paginator.num_pages)

        context['sf6_emissions'] = sf6_emissions
        context['total_co2'] = filtered_qs

        return context


class Sf6DetailView(LoginRequiredMixin, CompanyContextMixin, DetailView):
    model = Sf6
    template_name = 'envdata/scope_one_emission/sf6/sf6-emission.html'
    context_object_name = 'sf6_emission'


class Sf6CreateView(LoginRequiredMixin, CompanyContextMixin, CreateView):
    model = Sf6
    form_class = Sf6Form
    template_name = 'envdata/scope_one_emission/sf6/form-sf6.html'
    success_url = reverse_lazy('sf6_emissions')

    def get_form_kwargs(self):
        kwargs = super(Sf6CreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('sf6_emissions')


class Sf6UpdateView(LoginRequiredMixin, UpdateModeMixin, CompanyContextMixin, UpdateView):
    model = Sf6
    form_class = Sf6Form
    template_name = 'envdata/scope_one_emission/sf6/form-sf6.html'
    success_url = reverse_lazy('sf6_emissions')

    def get_form_kwargs(self):
        kwargs = super(Sf6UpdateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        return super().form_valid(form)


class Sf6DeleteView(LoginRequiredMixin, CompanyContextMixin, DeleteView):
    model = Sf6
    template_name = 'envdata/delete-universal.html'
    success_url = reverse_lazy('sf6_emissions')
