from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from envdata.mixins import UpdateModeMixin, CompanyContextMixin
from envdata.models import Refrigerant
from envdata.forms import RefrigerantForm
from django.contrib.auth.mixins import LoginRequiredMixin


class RefrigerantView(LoginRequiredMixin, CompanyContextMixin, ListView):
    model = Refrigerant
    template_name = 'envdata/scope_one_emission/refrigerant/refrigerant-emissions.html'
    context_object_name = 'refrigerants_emissions'


class RefrigerantDetailView(LoginRequiredMixin, CompanyContextMixin, DetailView):
    model = Refrigerant
    template_name = 'envdata/scope_one_emission/refrigerant/refrigerant-emission.html'
    context_object_name = 'refrigerant_emission'


class RefrigerantCreateView(LoginRequiredMixin, CompanyContextMixin, CreateView):
    model = Refrigerant
    form_class = RefrigerantForm
    template_name = 'envdata/scope_one_emission/refrigerant/form-refrigerant.html'
    success_url = reverse_lazy('refrigerant_emissions')

    def form_valid(self, form):
        form.instance.owner = self.request.user.profile
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('refrigerant_emissions')


class RefrigerantUpdateView(LoginRequiredMixin, UpdateModeMixin, CompanyContextMixin, UpdateView):
    model = Refrigerant
    form_class = RefrigerantForm
    template_name = 'envdata/scope_one_emission/refrigerant/form-refrigerant.html'
    success_url = reverse_lazy('refrigerant_emissions')


class RefrigerantDeleteView(LoginRequiredMixin, CompanyContextMixin, DeleteView):
    model = Refrigerant
    template_name = 'envdata/delete-universal.html'
    success_url = reverse_lazy('refrigerant_emissions')
