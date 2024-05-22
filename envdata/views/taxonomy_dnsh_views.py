from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from envdata.models import DoNotSeriousHarm
from envdata.forms import TaxonomyDnshForm
from envdata.mixins import CompanyContextMixin, UpdateModeMixin


class TaxonomyDnshListView(LoginRequiredMixin, CompanyContextMixin, ListView):
    model = DoNotSeriousHarm
    template_name = 'envdata/taxonomy/dnsh/all-dnsh.html'
    context_object_name = 'dnshs'


class TaxonomyDnshDetailView(LoginRequiredMixin, CompanyContextMixin, DetailView):
    model = DoNotSeriousHarm
    template_name = 'envdata/taxonomy/dnsh/single-dnsh.html'
    context_object_name = 'dnsh'


class TaxonomyDnshCreateView(LoginRequiredMixin, CompanyContextMixin, CreateView):
    model = DoNotSeriousHarm
    form_class = TaxonomyDnshForm
    template_name = 'envdata/taxonomy/dnsh/form-dnsh.html'
    success_url = reverse_lazy('dnshs')

    def form_valid(self, form):
        form.instance.owner = self.request.user.profile
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('dnshs')


class TaxonomyDnshUpdateView(LoginRequiredMixin, CompanyContextMixin, UpdateModeMixin, UpdateView):
    model = DoNotSeriousHarm
    form_class = TaxonomyDnshForm
    template_name = 'envdata/taxonomy/dnsh/form-dnsh.html'
    success_url = reverse_lazy('dnshs')


class TaxonomyDnshDeleteView(LoginRequiredMixin, CompanyContextMixin, DeleteView):
    model = DoNotSeriousHarm
    template_name = 'envdata/delete-universal.html'
    success_url = reverse_lazy('dnshs')
