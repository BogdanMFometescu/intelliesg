from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from envdata.models import TaxonomyTurnover
from envdata.forms import TaxonomyTurnoverForm
from envdata.mixins import CompanyContextMixin, UpdateModeMixin


class TaxonomyTurnoverListView(LoginRequiredMixin, CompanyContextMixin, ListView):
    model = TaxonomyTurnover
    template_name = 'envdata/taxonomy/turnover/turnovers.html'
    context_object_name = 'turnovers'


class TaxonomyTurnoverDetailView(LoginRequiredMixin, CompanyContextMixin, DetailView):
    model = TaxonomyTurnover
    template_name = 'envdata/taxonomy/turnover/turnover.html'
    context_object_name = 'turnover'


class TaxonomyTurnoverCreateView(LoginRequiredMixin, CompanyContextMixin, CreateView):
    model = TaxonomyTurnover
    form_class = TaxonomyTurnoverForm
    template_name = 'envdata/taxonomy/turnover/form-turnover.html'
    success_url = reverse_lazy('turnovers')

    def form_valid(self, form):
        form.instance.owner = self.request.user.profile
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('turnovers')


class TaxonomyTurnoverUpdateView(LoginRequiredMixin, CompanyContextMixin, UpdateModeMixin, UpdateView):
    model = TaxonomyTurnover
    form_class = TaxonomyTurnoverForm
    template_name = 'envdata/taxonomy/turnover/form-turnover.html'
    success_url = reverse_lazy('opexes')


class TaxonomyTurnoverDeleteView(LoginRequiredMixin, CompanyContextMixin, DeleteView):
    model = TaxonomyTurnover
    template_name = 'envdata/delete-universal.html'
    success_url = reverse_lazy('turnovers')
