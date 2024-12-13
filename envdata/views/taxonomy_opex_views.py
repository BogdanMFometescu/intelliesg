from django.views.generic import  DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from envdata.models import TaxonomyOpEx
from envdata.forms import TaxonomyOpexForm
from common.mixins import CompanyContextMixin, UpdateModeMixin
from .filters import TaxonomyOpeExFilter
from django_filters.views import FilterView
from django.db.models import Sum, F


class TaxonomyOpexListView(LoginRequiredMixin, CompanyContextMixin, FilterView):
    model = TaxonomyOpEx
    filterset_class = TaxonomyOpeExFilter
    template_name = 'envdata/taxonomy/opex/all-opex.html'
    context_object_name = 'opexs'

    def get_queryset(self):
        if self.request.user.is_staff:
            return super().get_queryset()
        return TaxonomyOpEx.objects.filter(profile__user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        filtered_qs = self.filterset.qs.annotate(total_eligible_opex=F('opex_eligible') + F('opex_aligned')).aggregate(
            total_opex=Sum('total_eligible_opex'))['total_opex'] or 0
        filtered_not_eligible = self.filterset.qs.annotate(total_non_eligible_opex=F('opex_non_eligible')).aggregate(
            total_non_eligiblex=Sum('total_non_eligible_opex'))['total_non_eligiblex'] or 0
        context['total_eligible_display'] = filtered_qs
        context['total_non_eligible'] = filtered_not_eligible
        return context


class TaxonomyOpexDetailView(LoginRequiredMixin, CompanyContextMixin, DetailView):
    model = TaxonomyOpEx
    template_name = 'envdata/taxonomy/opex/single-opex.html'
    context_object_name = 'opex'


class TaxonomyOpexCreateView(LoginRequiredMixin, CompanyContextMixin, CreateView):
    model = TaxonomyOpEx
    form_class = TaxonomyOpexForm
    template_name = 'envdata/taxonomy/opex/form-opex.html'
    success_url = reverse_lazy('opexs')

    def get_form_kwargs(self):
        kwargs = super(TaxonomyOpexCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('opexs')


class TaxonomyOpexUpdateView(LoginRequiredMixin, CompanyContextMixin, UpdateModeMixin, UpdateView):
    model = TaxonomyOpEx
    form_class = TaxonomyOpexForm
    template_name = 'envdata/taxonomy/opex/form-opex.html'
    success_url = reverse_lazy('opexs')

    def get_form_kwargs(self):
        kwargs = super(TaxonomyOpexUpdateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        return super().form_valid(form)


class TaxonomyOpexDeleteView(LoginRequiredMixin, CompanyContextMixin, DeleteView):
    model = TaxonomyOpEx
    template_name = 'envdata/delete-universal.html'
    success_url = reverse_lazy('opexs')
