from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from envdata.models import TaxonomyCapEx
from envdata.forms import TaxonomyCapexForm
from envdata.mixins import CompanyContextMixin, UpdateModeMixin
from .filters import TaxonomyCapExFilter
from django_filters.views import FilterView
from django.db.models import F, Sum


class TaxonomyCapexListView(LoginRequiredMixin, CompanyContextMixin, FilterView):
    model = TaxonomyCapEx
    filterset_class = TaxonomyCapExFilter
    template_name = 'envdata/taxonomy/capex/all-capex.html'
    context_object_name = 'capexs'

    def get_queryset(self):
        if self.request.user.is_staff:
            return super().get_queryset()
        return TaxonomyCapEx.objects.filter(profile__user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        filtered_qs = \
            self.filterset.qs.annotate(total_eligible_capex=F('capex_eligible') + F('capex_aligned')).aggregate(
                total_eligible=Sum('total_eligible_capex'))['total_eligible'] or 0
        capex_not_aligned = self.filterset.qs.annotate(total_non_eligible_capex=F('capex_non_eligible')).aggregate(
            total_non_eligible=Sum('total_non_eligible_capex'))['total_non_eligible'] or 0
        context['total_capex_display'] = filtered_qs
        context['total_non_eligible'] = capex_not_aligned
        return context


class TaxonomyCapexDetailView(LoginRequiredMixin, CompanyContextMixin, DetailView):
    model = TaxonomyCapEx
    template_name = 'envdata/taxonomy/capex/single-capex.html'
    context_object_name = 'capex'


class TaxonomyCapexCreateView(LoginRequiredMixin, CompanyContextMixin, CreateView):
    model = TaxonomyCapEx
    form_class = TaxonomyCapexForm
    template_name = 'envdata/taxonomy/capex/form-capex.html'
    success_url = reverse_lazy('capexs')

    def get_form_kwargs(self):
        kwargs = super(TaxonomyCapexCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('capexs')


class TaxonomyCapexUpdateView(LoginRequiredMixin, CompanyContextMixin, UpdateModeMixin, UpdateView):
    model = TaxonomyCapEx
    form_class = TaxonomyCapexForm
    template_name = 'envdata/taxonomy/capex/form-capex.html'
    success_url = reverse_lazy('capexs')

    def get_form_kwargs(self):
        kwargs = super(TaxonomyCapexUpdateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        return super().form_valid(form)




class TaxonomyCapexDeleteView(LoginRequiredMixin, CompanyContextMixin, DeleteView):
    model = TaxonomyCapEx
    template_name = 'envdata/delete-universal.html'
    success_url = reverse_lazy('capexs')
