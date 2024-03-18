from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from envdata.mixins import UpdateModeMixin, CompanyContextMixin
from envdata.models import Sf6
from envdata.forms import Sf6Form
from django.contrib.auth.mixins import LoginRequiredMixin


class Sf6ListView(LoginRequiredMixin, CompanyContextMixin, ListView):
    model = Sf6
    template_name = 'envdata/scope_one_emission/sf6/sf6-emissions.html'
    context_object_name = 'sf6_emissions'


class Sf6DetailView(LoginRequiredMixin, CompanyContextMixin, DetailView):
    model = Sf6
    template_name = 'envdata/scope_one_emission/sf6/sf6-emission.html'
    context_object_name = 'sf6_emission'


class Sf6CreateView(LoginRequiredMixin, CompanyContextMixin, CreateView):
    model = Sf6
    form_class = Sf6Form
    template_name = 'envdata/scope_one_emission/sf6/form-sf6.html'
    success_url = reverse_lazy('sf6_emissions')

    def form_valid(self, form):
        form.instance.owner = self.request.user.profile
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('sf6_emissions')


class Sf6UpdateView(LoginRequiredMixin, UpdateModeMixin, CompanyContextMixin, UpdateView):
    model = Sf6
    form_class = Sf6Form
    template_name = 'envdata/scope_one_emission/sf6/form-sf6.html'
    success_url = reverse_lazy('sf6_emissions')


class Sf6DeleteView(LoginRequiredMixin, CompanyContextMixin, DeleteView):
    model = Sf6
    template_name = 'envdata/delete-universal.html'
    success_url = reverse_lazy('sf6_emissions')
