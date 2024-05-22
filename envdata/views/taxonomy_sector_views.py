from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from envdata.models import TaxonomySector
from envdata.forms import TaxonomySectorForm
from envdata.mixins import CompanyContextMixin, UpdateModeMixin


class TaxonomySectorListView(LoginRequiredMixin, CompanyContextMixin, ListView):
    model = TaxonomySector
    template_name = 'envdata/taxonomy/sector/sectors.html'
    context_object_name = 'sectors'


class TaxonomySectorDetailView(LoginRequiredMixin, CompanyContextMixin, DetailView):
    model = TaxonomySector
    template_name = 'envdata/taxonomy/sector/sector.html'
    context_object_name = 'sector'


class TaxonomySectorCreateView(LoginRequiredMixin, CompanyContextMixin, CreateView):
    model = TaxonomySector
    form_class = TaxonomySectorForm
    template_name = 'envdata/taxonomy/sector/form-sector.html'
    success_url = reverse_lazy('sectors')

    def form_valid(self, form):
        form.instance.owner = self.request.user.profile
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('sectors')


class TaxonomySectorUpdateView(LoginRequiredMixin, CompanyContextMixin, UpdateModeMixin, UpdateView):
    model = TaxonomySector
    form_class = TaxonomySectorForm
    template_name = 'envdata/taxonomy/sector/form-sector.html'
    success_url = reverse_lazy('sectors')


class TaxonomySectorDeleteView(LoginRequiredMixin, CompanyContextMixin, DeleteView):
    model = TaxonomySector
    template_name = 'envdata/delete-universal.html'
    success_url = reverse_lazy('sectors')
