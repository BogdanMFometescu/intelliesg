from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from envdata.models import TaxonomyTurnover
from envdata.forms import TaxonomyTurnoverForm
from common.mixins import CompanyContextMixin, UpdateModeMixin
from .filters import TaxonomyTurnoverFilter
from django_filters.views import FilterView
from django.db.models import Sum, F


class TaxonomyTurnoverListView(LoginRequiredMixin, CompanyContextMixin, FilterView):
    model = TaxonomyTurnover
    filterset_class = TaxonomyTurnoverFilter
    template_name = 'envdata/taxonomy/turnover/turnovers.html'
    context_object_name = 'turnovers'

    def get_queryset(self):
        if self.request.user.is_staff:
            return super().get_queryset()
        return TaxonomyTurnover.objects.filter(profile__user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        filtered_qs = \
        self.filterset.qs.annotate(total_eligible_turnover=F('turnover_eligible') + F('turnover_aligned')).aggregate(
            total_eligible=Sum('total_eligible_turnover'))['total_eligible'] or 0
        filtered_not_eligible = \
        self.filterset.qs.annotate(total_non_eligible_turnover=F('turnover_non_eligible')).aggregate(
            total_non_eligible=Sum('total_non_eligible_turnover'))['total_non_eligible'] or 0
        context['total_eligible_display'] = filtered_qs
        context['total_non_eligible'] = filtered_not_eligible
        return context


class TaxonomyTurnoverDetailView(LoginRequiredMixin, CompanyContextMixin, DetailView):
    model = TaxonomyTurnover
    template_name = 'envdata/taxonomy/turnover/turnover.html'
    context_object_name = 'turnover'


class TaxonomyTurnoverCreateView(LoginRequiredMixin, CompanyContextMixin, CreateView):
    model = TaxonomyTurnover
    form_class = TaxonomyTurnoverForm
    template_name = 'envdata/taxonomy/turnover/form-turnover.html'
    success_url = reverse_lazy('turnovers')

    def get_form_kwargs(self):
        kwargs = super(TaxonomyTurnoverCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('turnovers')


class TaxonomyTurnoverUpdateView(LoginRequiredMixin, CompanyContextMixin, UpdateModeMixin, UpdateView):
    model = TaxonomyTurnover
    form_class = TaxonomyTurnoverForm
    template_name = 'envdata/taxonomy/turnover/form-turnover.html'
    success_url = reverse_lazy('turnovers')

    def get_form_kwargs(self):
        kwargs = super(TaxonomyTurnoverUpdateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        return super().form_valid(form)

class TaxonomyTurnoverDeleteView(LoginRequiredMixin, CompanyContextMixin, DeleteView):
    model = TaxonomyTurnover
    template_name = 'envdata/delete-universal.html'
    success_url = reverse_lazy('turnovers')
