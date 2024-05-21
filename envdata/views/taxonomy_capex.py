from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from envdata.models import TaxonomyCapEx
from envdata.forms import TaxonomyCapexForm
from envdata.mixins import CompanyContextMixin, UpdateModeMixin


class TaxonomyCapexListView(LoginRequiredMixin, CompanyContextMixin, ListView):
    model = TaxonomyCapEx
    template_name = ''
    context_object_name = 'capexs'


class TaxonomyCapexDetailView(LoginRequiredMixin, CompanyContextMixin, DetailView):
    model = TaxonomyCapEx
    template_name = ''
    context_object_name = 'capex'


class TaxonomyCapexCreateView(LoginRequiredMixin, CompanyContextMixin, CreateView):
    model = TaxonomyCapEx
    form_class = TaxonomyCapexForm
    template_name = ''
    success_url = reverse_lazy('capexs')

    def form_valid(self, form):
        form.instance.owner = self.request.user.profile
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('capexs')


class TaxonomyCapexUpdateView(LoginRequiredMixin, CompanyContextMixin, UpdateModeMixin, UpdateView):
    model = TaxonomyCapEx
    form_class = TaxonomyCapexForm
    template_name = ''
    success_url = reverse_lazy('capexs')


class TaxonomyCapexDeleteView(LoginRequiredMixin, CompanyContextMixin, DeleteView):
    model = TaxonomyCapEx
    template_name = ''
    success_url = reverse_lazy('capexs')
