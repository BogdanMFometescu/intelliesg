from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from envdata.mixins import UpdateModeMixin, CompanyContextMixin
from envdata.models import Refrigerant
from envdata.forms import RefrigerantForm


class RefrigerantView(CompanyContextMixin, ListView):
    model = Refrigerant
    template_name = 'envdata/scope_one_emission/refrigerant/refrigerant-emissions.html'
    context_object_name = 'refrigerants_emissions'


class RefrigerantDetailView(CompanyContextMixin, DetailView):
    model = Refrigerant
    template_name = 'envdata/scope_one_emission/refrigerant/refrigerant-emission.html'
    context_object_name = 'refrigerant_emission'


class RefrigerantCreateView(CompanyContextMixin, CreateView):
    model = Refrigerant
    form_class = RefrigerantForm
    template_name = 'envdata/scope_one_emission/refrigerant/form-refrigerant.html'
    success_url = reverse_lazy('refrigerant_emissions')

    def form_valid(self, form):
        return super().form_valid(form)


class RefrigerantUpdateView(UpdateModeMixin, CompanyContextMixin, UpdateView):
    model = Refrigerant
    form_class = RefrigerantForm
    template_name = 'envdata/scope_one_emission/refrigerant/form-refrigerant.html'
    success_url = reverse_lazy('refrigerant_emissions')


class RefrigerantDeleteView(CompanyContextMixin, DeleteView):
    model = Refrigerant
    template_name = 'envdata/delete-universal.html'
    success_url = reverse_lazy('refrigerant_emissions')
