from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from envdata.mixins import UpdateModeMixin
from envdata.models import Fuel
from envdata.forms import FuelForm


class FuelListView(ListView):
    model = Fuel
    template_name = 'envdata/scope_one_emission/fuel/fuel-emissions.html'
    context_object_name = 'fuel_emissions'

    def get_queryset(self):
        return Fuel.objects.all().order_by('month','year')


class FuelDetailView(DetailView):
    model = Fuel
    template_name = 'envdata/scope_one_emission/fuel/fuel-emission.html'
    context_object_name = 'fuel_emission'


class FuelCreateView(CreateView):
    model = Fuel
    form_class = FuelForm
    template_name = 'envdata/scope_one_emission/fuel/form-fuel.html'
    success_url = reverse_lazy('fuel_emissions')

    def form_valid(self, form):
        return super().form_valid(form)


class FuelUpdateView(UpdateModeMixin, UpdateView):
    model = Fuel
    form_class = FuelForm
    template_name = 'envdata/scope_one_emission/fuel/form-fuel.html'
    success_url = reverse_lazy('fuel_emissions')


class FuelDeleteView(DeleteView):
    model = Fuel
    template_name = 'envdata/delete-universal.html'
    success_url = reverse_lazy('fuel_emissions')
