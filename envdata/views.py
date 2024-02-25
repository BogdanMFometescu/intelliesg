from envdata.models import (
    Fuel,
    Sf6,
    Refrigerant,
    Energy, Travel)

from envdata.forms import (

    FuelForm,
    Sf6Form,
    RefrigerantForm,
    EnergyForm,
    TravelForm)

from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from envdata.mixins import UpdateModeMixin


class FuelListView(ListView):
    model = Fuel
    template_name = 'envdata/scope_one_emission/fuel/fuel-emissions.html'
    context_object_name = 'fuel_emissions'


class FuelDetailView(DetailView):
    model = Fuel
    template_name = 'envdata/scope_one_emission/fuel/single-fuel-emission.html'
    context_object_name = 'fuel_emission'


class FuelCreateView(CreateView):
    model = Fuel
    form_class = FuelForm
    template_name = 'envdata/scope_one_emission/fuel/form-fuel-emission.html'
    success_url = reverse_lazy('fuel_emissions')

    def form_valid(self, form):
        return super(FuelCreateView, self).form_valid(form)


class FuelUpdateView(UpdateModeMixin, UpdateView):
    model = Fuel
    form_class = FuelForm
    template_name = 'envdata/scope_one_emission/fuel/form-fuel-emission.html'
    success_url = reverse_lazy('fuel_emissions')


class FuelDeleteView(DeleteView):
    model = Fuel
    template_name = 'envdata/delete-universal.html'
    success_url = reverse_lazy('fuel_emissions')


class Sf6EmissionListView(ListView):
    model = Sf6
    template_name = 'envdata/scope_one_emission/sf6/sf6-emissions.html'
    context_object_name = 'sf6_emissions'


class Sf6EmissionDetailView(DetailView):
    model = Sf6
    template_name = 'envdata/scope_one_emission/sf6/sf6-emission.html'
    context_object_name = 'sf6_emission'


class Sf6EmissionCreateView(CreateView):
    model = Sf6
    form_class = Sf6Form
    template_name = 'envdata/scope_one_emission/sf6/form-sf6-emission.html'
    success_url = reverse_lazy('sf6_emissions')

    def form_valid(self, form):
        return super(Sf6EmissionCreateView, self).form_valid(form)


class Sf6EmissionUpdateView(UpdateModeMixin, UpdateView):
    model = Sf6
    form_class = Sf6Form
    template_name = 'envdata/scope_one_emission/sf6/form-sf6-emission.html'
    success_url = reverse_lazy('sf6_emissions')


class Sf6EmissionDeleteView(DeleteView):
    model = Sf6
    template_name = 'envdata/delete-universal.html'
    success_url = reverse_lazy('sf6_emissions')


class RefrigerantsEmissionsView(ListView):
    model = Refrigerant
    template_name = 'envdata/scope_one_emission/refrigerant/refrigerant-emissions.html'
    context_object_name = 'refrigerants_emissions'


class RefrigerantsEmissionsDetailView(DetailView):
    model = Refrigerant
    template_name = 'envdata/scope_one_emission/refrigerant/refrigerant-emissions.html'
    context_object_name = 'refrigerant_emission'


class RefrigerantsEmissionsCreateView(CreateView):
    model = Refrigerant
    form_class = RefrigerantForm
    template_name = 'envdata/scope_one_emission/refrigerant/form-refrigerant-emission.html'
    success_url = reverse_lazy('refrigerants_emissions')

    def form_valid(self, form):
        return super(RefrigerantsEmissionsCreateView).form_valid(form)


class RefrigerantsEmissionsUpdateView(UpdateModeMixin, UpdateView):
    model = Refrigerant
    form_class = RefrigerantForm
    template_name = 'envdata/scope_one_emission/refrigerant/form-refrigerant-emission.html'
    success_url = reverse_lazy('refrigerant_emissions')


class RefrigerantsEmissionsDeleteView(DeleteView):
    model = Refrigerant
    template_name = 'envdata/delete-universal.html'
    success_url = reverse_lazy('refrigerant_emissions')


class EnergyAcquisitionListView(ListView):
    model = Energy
    template_name = 'envdata/scope_two_emission/energy_aq/energy-acquisitions-emission.html'
    context_object_name = 'energy_acquisitions'


class EnergyAcquisitionDetailView(DetailView):
    model = Energy
    template_name = 'envdata/scope_two_emission/energy_aq/single-energy-acquisition-emission.html'
    context_object_name = 'energy_acquisition'


class EnergyAcquisitionCreateView(CreateView):
    model = Energy
    form_class = EnergyForm
    template_name = 'envdata/scope_two_emission/energy_aq/form-energy-acquisition-emission.html'
    success_url = reverse_lazy('energy_acquisitions')

    def form_valid(self, form):
        return super(EnergyAcquisitionCreateView).form_valid(form)


class EnergyAcquisitionUpdateView(UpdateModeMixin, UpdateView):
    model = Energy
    form_class = EnergyForm
    template_name = 'envdata/scope_two_emission/energy_aq/form-energy-acquisition-emission.html'
    success_url = reverse_lazy('energy_acquisitions')


class EnergyAcquisitionDeleteView(DeleteView):
    model = Energy
    template_name = 'envdata/delete-universal.html'
    success_url = reverse_lazy('energy_acquisitions')


class TravelEmissionsListView(ListView):
    model = Travel
    template_name = 'envdata/scope_one_emission/travel/travels.html'
    context_object_name = 'travel_emissions'


class TravelEmissionsDetailView(DetailView):
    model = Travel
    template_name = 'envdata/scope_one_emission/travel/single-travel.html'
    context_object_name = 'travel_emission'


class TravelEmissionsCreateView(CreateView):
    model = Travel
    form_class = TravelForm
    template_name = 'envdata/scope_one_emission/travel/form-travel.html'
    success_url = reverse_lazy('travel_emissions')

    def form_valid(self, form):
        return super(TravelEmissionsCreateView).form_valid(form)


class TravelEmissionsUpdateView(UpdateModeMixin, UpdateView):
    model = Travel
    form_class = TravelForm
    template_name = 'envdata/scope_one_emission/travel/form-travel.html'
    success_url = reverse_lazy('travel_emissions')


class TravelDeleteView(DeleteView):
    model = Travel
    template_name = 'envdata/delete-universal.html'
    success_url = reverse_lazy('travel_emissions')
