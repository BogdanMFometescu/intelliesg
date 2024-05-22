from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from envdata.models import TaxonomyOpEx
from envdata.forms import TaxonomyOpexForm
from envdata.mixins import CompanyContextMixin, UpdateModeMixin


class TaxonomyOpexListView(LoginRequiredMixin, CompanyContextMixin, ListView):
    model = TaxonomyOpEx
    template_name = 'envdata/taxonomy/opex/all-opex.html'
    context_object_name = 'turnovers'


class TaxonomyOpexDetailView(LoginRequiredMixin, CompanyContextMixin, DetailView):
    model = TaxonomyOpEx
    template_name = 'envdata/taxonomy/opex/single-opex.html'
    context_object_name = 'turnover'


class TaxonomyOpexCreateView(LoginRequiredMixin, CompanyContextMixin, CreateView):
    model = TaxonomyOpEx
    form_class = TaxonomyOpexForm
    template_name = 'envdata/taxonomy/opex/form-opex.html'
    success_url = reverse_lazy('turnovers')

    def form_valid(self, form):
        form.instance.owner = self.request.user.profile
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('turnovers')


class TaxonomyOpexUpdateView(LoginRequiredMixin, CompanyContextMixin, UpdateModeMixin, UpdateView):
    model = TaxonomyOpEx
    form_class = TaxonomyOpexForm
    template_name = 'envdata/taxonomy/opex/form-opex.html'
    success_url = reverse_lazy('turnovers')


class TaxonomyOpexDeleteView(LoginRequiredMixin, CompanyContextMixin, DeleteView):
    model = TaxonomyOpEx
    template_name = 'envdata/delete-universal.html'
    success_url = reverse_lazy('turnovers')
