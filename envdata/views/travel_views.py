from django.urls import reverse_lazy
from django.views.generic import (DetailView, CreateView, UpdateView, DeleteView)
from common.mixins import UpdateModeMixin, CompanyContextMixin
from envdata.models import Travel
from envdata.forms import TravelForm
from .filters import TravelTypeFilter
from django.contrib.auth.mixins import LoginRequiredMixin
from django_filters.views import FilterView
from django.db.models import Sum, F
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class TravelListView(LoginRequiredMixin, CompanyContextMixin, FilterView):
    model = Travel
    filterset_class = TravelTypeFilter
    template_name = 'envdata/scope_one_emission/travel/travels.html'
    context_object_name = 'travels'
    paginate_by = 12

    def get_queryset(self):
        if self.request.user.is_staff:
            return super().get_queryset()
        return Travel.objects.filter(profile__user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        filtered_qs = \
            self.filterset.qs.annotate(co2_for_travel=F('distance') * F('emission_factor')).aggregate(
                total_co2=Sum('co2_for_travel'))['total_co2'] or 0

        paginator = Paginator(self.filterset.qs, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            travels = paginator.page(page)
        except PageNotAnInteger:
            travels = paginator.page(1)
        except EmptyPage:
            travels = paginator.page(paginator.num_pages)

        context['travels'] = travels
        context['total_co2'] = filtered_qs

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

    def get_form_kwargs(self):
        kwargs = super(TravelCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('travels')


class TravelUpdateView(LoginRequiredMixin, UpdateModeMixin, CompanyContextMixin, UpdateView):
    model = Travel
    form_class = TravelForm
    template_name = 'envdata/scope_one_emission/travel/form-travel.html'
    success_url = reverse_lazy('travels')

    def get_form_kwargs(self):
        kwargs = super(TravelUpdateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        return super().form_valid(form)


class TravelDeleteView(LoginRequiredMixin, CompanyContextMixin, DeleteView):
    model = Travel
    template_name = 'envdata/delete-universal.html'
    success_url = reverse_lazy('travels')
