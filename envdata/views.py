from envdata.forms import (EmissionForm,
                           FuelEmissionForm,
                           Sf6EmissionForm,
                           RefrigerantEmissionForm,
                           EnergyAcquisitionForm,
                           TravelForm)
from envdata.models import (Emission,
                            FuelEmission,
                            Sf6Emission,
                            RefrigerantEmission,
                            EnergyAcquisition, Travel)

from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from envdata.mixins import UpdateModeMixin


class EmissionListView(ListView):
    model = Emission
    template_name = 'envdata/emissions.html'
    context_object_name = 'emissions'


class EmissionDetailView(DetailView):
    model = Emission
    template_name = 'envdata/single-emission.html'
    context_object_name = 'emission'


class EmissionCreateView(CreateView):
    model = Emission
    form_class = EmissionForm
    template_name = 'envdata/form-emission.html'
    success_url = reverse_lazy('emissions')

    def form_valid(self, form):
        return super(EmissionCreateView, self).form_valid(form)


class EmissionUpdateView(UpdateModeMixin, UpdateView):
    model = Emission
    form_class = EmissionForm
    template_name = 'envdata/form-emission.html'
    success_url = reverse_lazy('emissions')


class EmissionDeleteView(DeleteView):
    model = Emission
    template_name = 'envdata/delete-universal.html'
    success_url = reverse_lazy('emissions')


class FuelListView(ListView):
    model = FuelEmission
    template_name = 'envdata/scope_one_emission/fuel/fuel-emissions.html'
    context_object_name = 'fuel_emissions'


class FuelDetailView(DetailView):
    model = FuelEmission
    template_name = 'envdata/scope_one_emission/fuel/single-fuel-emission.html'
    context_object_name = 'fuel_emission'


class FuelCreateView(CreateView):
    model = FuelEmission
    form_class = FuelEmissionForm
    template_name = 'envdata/scope_one_emission/fuel/form-fuel-emission.html'
    success_url = reverse_lazy('fuel_emissions')

    def form_valid(self, form):
        return super(FuelCreateView, self).form_valid(form)


class FuelUpdateView(UpdateModeMixin, UpdateView):
    model = FuelEmission
    form_class = FuelEmissionForm
    template_name = 'envdata/scope_one_emission/fuel/form-fuel-emission.html'
    success_url = reverse_lazy('fuel_emissions')


class FuelDeleteView(DeleteView):
    model = FuelEmission
    template_name = 'envdata/delete-universal.html'
    success_url = reverse_lazy('fuel_emissions')


class Sf6EmissionListView(ListView):
    model = Sf6Emission
    template_name = 'envdata/scope_one_emission/sf6/sf6-emissions.html'
    context_object_name = 'sf6_emissions'


class Sf6EmissionDetailView(DetailView):
    model = Sf6Emission
    template_name = 'envdata/scope_one_emission/sf6/sf6-emission.html'
    context_object_name = 'sf6_emission'


class Sf6EmissionCreateView(CreateView):
    model = Sf6Emission
    form_class = Sf6EmissionForm
    template_name = 'envdata/scope_one_emission/sf6/form-sf6-emission.html'
    success_url = reverse_lazy('sf6_emissions')

    def form_valid(self, form):
        return super(Sf6EmissionCreateView, self).form_valid(form)


class Sf6EmissionUpdateView(UpdateModeMixin, UpdateView):
    model = Sf6Emission
    form_class = Sf6EmissionForm
    template_name = 'envdata/scope_one_emission/sf6/form-sf6-emission.html'
    success_url = reverse_lazy('sf6_emissions')


class Sf6EmissionDeleteView(DeleteView):
    model = Sf6Emission
    template_name = 'envdata/delete-universal.html'
    success_url = reverse_lazy('sf6_emissions')


class RefrigerantsEmissionsView(ListView):
    model = RefrigerantEmission
    template_name = 'envdata/scope_one_emission/refrigerant/refrigerant-emissions.html'
    context_object_name = 'refrigerants_emissions'


class RefrigerantsEmissionsDetailView(DetailView):
    model = RefrigerantEmission
    template_name = 'envdata/scope_one_emission/refrigerant/refrigerant-emissions.html'
    context_object_name = 'refrigerant_emission'


class RefrigerantsEmissionsCreateView(CreateView):
    model = RefrigerantEmission
    form_class = RefrigerantEmissionForm
    template_name = 'envdata/scope_one_emission/refrigerant/form-refrigerant-emission.html'
    success_url = reverse_lazy('refrigerants_emissions')

    def form_valid(self, form):
        return super(RefrigerantsEmissionsCreateView).form_valid(form)


class RefrigerantsEmissionsUpdateView(UpdateModeMixin, UpdateView):
    model = RefrigerantEmission
    form_class = RefrigerantEmissionForm
    template_name = 'envdata/scope_one_emission/refrigerant/form-refrigerant-emission.html'
    success_url = reverse_lazy('refrigerant_emissions')


class RefrigerantsEmissionsDeleteView(DeleteView):
    model = RefrigerantEmission
    template_name = 'envdata/delete-universal.html'
    success_url = reverse_lazy('refrigerant_emissions')


class EnergyAcquisitionListView(ListView):
    model = EnergyAcquisition
    template_name = 'envdata/scope_two_emission/energy_aq/energy-acquisitions-emission.html'
    context_object_name = 'energy_acquisitions'


class EnergyAcquisitionDetailView(DetailView):
    model = EnergyAcquisition
    template_name = 'envdata/scope_two_emission/energy_aq/single-energy-acquisition-emission.html'
    context_object_name = 'energy_acquisition'


class EnergyAcquisitionCreateView(CreateView):
    model = EnergyAcquisition
    form_class = EnergyAcquisitionForm
    template_name = 'envdata/scope_two_emission/energy_aq/form-energy-acquisition-emission.html'
    success_url = reverse_lazy('energy_acquisitions')

    def form_valid(self, form):
        return super(EnergyAcquisitionCreateView).form_valid(form)


class EnergyAcquisitionUpdateView(UpdateModeMixin, UpdateView):
    model = EnergyAcquisition
    form_class = EnergyAcquisitionForm
    template_name = 'envdata/scope_two_emission/energy_aq/form-energy-acquisition-emission.html'
    success_url = reverse_lazy('energy_acquisitions')


class EnergyAcquisitionDeleteView(DeleteView):
    model = EnergyAcquisition
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
