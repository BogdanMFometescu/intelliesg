from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from envdata.mixins import UpdateModeMixin, CompanyContextMixin
from envdata.models import Travel
from envdata.forms import TravelForm
from django.contrib.auth.mixins import LoginRequiredMixin


class TravelListView(LoginRequiredMixin, CompanyContextMixin, ListView):
    model = Travel
    template_name = 'envdata/scope_one_emission/travel/travels.html'
    context_object_name = 'travels'


class TravelDetailView(LoginRequiredMixin, CompanyContextMixin, DetailView):
    model = Travel
    template_name = 'envdata/scope_one_emission/travel/travel.html'
    context_object_name = 'travel'


class TravelCreateView(LoginRequiredMixin, CompanyContextMixin, CreateView):
    model = Travel
    form_class = TravelForm
    template_name = 'envdata/scope_one_emission/travel/form-travel.html'
    success_url = reverse_lazy('travels')

    def form_valid(self, form):
        form.instance.owner = self.request.user.profile
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('travels')


class TravelUpdateView(LoginRequiredMixin, UpdateModeMixin, CompanyContextMixin, UpdateView):
    model = Travel
    form_class = TravelForm
    template_name = 'envdata/scope_one_emission/travel/form-travel.html'
    success_url = reverse_lazy('travels')


class TravelDeleteView(LoginRequiredMixin, CompanyContextMixin, DeleteView):
    model = Travel
    template_name = 'envdata/delete-universal.html'
    success_url = reverse_lazy('travels')
