from django.shortcuts import render, redirect

from envdata.forms import (EmissionForm,
                           FuelEmissionForm,
                           Sf6EmissionForm,
                           RefrigerantEmissionForm,
                           EnergyAcquisitionForm,
                           DistanceCalculationForm)
from envdata.models import (Emission,
                            FuelEmission,
                            Sf6Emission,
                            RefrigerantEmission,
                            EnergyAcquisition, DistanceCalculation)

from django.shortcuts import get_object_or_404


# EMISSIONS
def emissions(request):
    all_emissions = Emission.objects.all()
    context = {'emissions': all_emissions}
    return render(request, 'envdata/emissions.html', context)


def emission(request, pk):
    single_emission = get_object_or_404(Emission, id=pk)
    context = {'emission': single_emission}
    return render(request, 'envdata/single-emission.html', context)


def create_emission(request):
    form = EmissionForm()
    if request.method == 'POST':
        form = EmissionForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('emissions')
    context = {'form': form}
    return render(request, 'envdata/form-emission.html', context)


def update_emission(request, pk):
    updated_emission = get_object_or_404(Emission, id=pk)
    form = EmissionForm(instance=updated_emission)
    if request.method == 'POST':
        form = EmissionForm(request.POST or None, instance=updated_emission)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'envdata/form-emission.html', context)


def delete_emission(request, pk):
    deleted_emission = get_object_or_404(Emission, id=pk)
    form = FuelEmissionForm(instance=deleted_emission)
    if request.method == 'POST':
        deleted_emission.delete()
    context = {'object': form}

    return render(request, 'envdata/delete-universal.html', context)


# SCOPE 1 FUEL EMISSIONS
def fuel_emissions(request):
    all_fuel_emissions = FuelEmission.objects.all()
    context = {'fuel_emissions': all_fuel_emissions}
    return render(request, 'envdata/scope_one_emission/fuel/fuel-emissions.html', context)


def fuel_emission(request, pk):
    single_fuel_emission = get_object_or_404(FuelEmission, id=pk)
    context = {'fuel_emission': single_fuel_emission}
    return render(request, 'envdata/scope_one_emission/fuel/single-fuel-emission.html', context)


def create_fuel_emission(request):
    form = FuelEmissionForm()
    if request.method == 'POST':
        form = FuelEmissionForm(request.POST or None)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'envdata/scope_one_emission/fuel/form-fuel-emission.html', context)


def update_fuel_emission(request, pk):
    updated_fuel_emission = get_object_or_404(FuelEmission, id=pk)
    form = FuelEmissionForm(instance=updated_fuel_emission)
    if request.method == 'POST':
        form = FuelEmissionForm(request.POST or None, instance=updated_fuel_emission)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'envdata/scope_one_emission/fuel/form-fuel-emission.html', context)


def delete_fuel_emission(request, pk):
    deleted_fuel_emission = get_object_or_404(FuelEmission, id=pk)
    form = FuelEmissionForm(instance=deleted_fuel_emission)
    if request.method == 'POST':
        deleted_fuel_emission.delete()
    context = {'form': form}
    return render(request, 'envdata/delete-universal.html', context)


# SCOPE 1 SG6 EMISSIONS

def sf6_emissions(request):
    all_sf6_emissions = Sf6Emission.objects.all()
    context = {'all_sf6_emissions': all_sf6_emissions}
    return render(request, 'envdata/scope_one_emission/sf6/sf6-emissions.html', context)


def sf6_emission(request, pk):
    single_sf6_emission = get_object_or_404(Sf6Emission, id=pk)
    context = {'single_sf6_emission': single_sf6_emission}
    return render(request, 'envdata/scope_one_emission/sf6/sf6-emission.html', context)


def create_sf6_emission(request):
    form = Sf6EmissionForm()
    if request.method == 'POST':
        form = Sf6EmissionForm(request.POST or None)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'envdata/scope_one_emission/sf6/form-sf6-emission.html', context)


def update_sf6_emission(request, pk):
    updated_sf6_emission = get_object_or_404(Sf6Emission, id=pk)
    form = Sf6EmissionForm(instance=updated_sf6_emission)
    if request.method == 'POST':
        form = Sf6EmissionForm(request.POST or None, instance=updated_sf6_emission)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'envdata/scope_one_emission/sf6/form-sf6-emission.html', context)


def delete_sf6_emission(request, pk):
    deleted_sf6_emission = get_object_or_404(Sf6Emission, id=pk)
    form = Sf6EmissionForm(instance=deleted_sf6_emission)
    if request.method == 'POST':
        deleted_sf6_emission.delete()
    context = {'object': form}
    return render(request, 'envdata/delete-universal.html', context)


# SCOPE 1 REFRIGERANTS EMISSIONS

def refrigerants_emissions(request):
    refrigerants = RefrigerantEmission.objects.all()
    context = {'refrigerants': refrigerants}
    return render(request, 'envdata/scope_one_emission/refrigerant/refrigerant-emissions.html', context)


def refrigerants_emission(request, pk):
    refrigerant = get_object_or_404(RefrigerantEmission, id=pk)
    context = {'refrigerant': refrigerant}
    return render(request, 'envdata/scope_one_emission/refrigerant/refrigerant-emission.html', context)


def create_refrigerants_emission(request):
    form = RefrigerantEmissionForm()
    if request.method == 'POST':
        form = RefrigerantEmissionForm(request.POST or None)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'envdata/scope_one_emission/refrigerant/form-refrigerant-emission.html', context)


def update_refrigerants_emission(request, pk):
    updated_refrigerant = get_object_or_404(RefrigerantEmission, id=pk)
    form = RefrigerantEmissionForm(instance=updated_refrigerant)
    if request.method == 'POST':
        form = RefrigerantEmissionForm(request.POST or None, instance=updated_refrigerant)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'envdata/scope_one_emission/refrigerant/form-refrigerant-emission.html', context)


def delete_refrigerants_emission(request, pk):
    deleted_refrigerant = get_object_or_404(RefrigerantEmission, id=pk)
    form = RefrigerantEmissionForm(instance=deleted_refrigerant)
    if request.method == 'POST':
        deleted_refrigerant.delete()
    context = {'object': form}
    return render(request, 'envdata/delete-universal.html', context)


# SCOPE 2 - ACQUISITIONS
def energy_acquisitions(request):
    acquisitions = EnergyAcquisition.objects.all()
    context = {'acquisitions': acquisitions}
    return render(request, 'envdata/scope_two_emission/energy_aq/energy-acquisitions-emission.html', context)


def energy_acquisition(request, pk):
    acquisition = get_object_or_404(EnergyAcquisition, id=pk)
    context = {'acquisition': acquisition}
    return render(request, 'envdata/scope_two_emission/energy_aq/single-energy-acquisition-emission.html', context)


def create_energy_acquisition(request):
    form = EnergyAcquisitionForm()
    if request.method == 'POST':
        form = EnergyAcquisitionForm(request.POST or None)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'envdata/scope_two_emission/energy_aq/form-energy-acquisition-emission.html', context)


def update_energy_acquisition(request, pk):
    updated_energy_aq = get_object_or_404(EnergyAcquisition, id=pk)
    form = EnergyAcquisitionForm(instance=updated_energy_aq)
    if request.method == 'POST':
        form = EnergyAcquisitionForm(request.POST or None, instance=updated_energy_aq)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'envdata/scope_two_emission/energy_aq/form-energy-acquisition-emission.html', context)


def delete_energy_acquisition(request, pk):
    deleted_energy_aq = get_object_or_404(EnergyAcquisition, id=pk)
    form = EnergyAcquisitionForm(instance=deleted_energy_aq)
    if request.method == 'POST':
        deleted_energy_aq.delete()
    context = {'object': form}
    return render(request, 'envdata/delete-universal.html', context)


def distances(request):
    all_distances = DistanceCalculation.objects.all()
    context = {'all_distances': all_distances}
    return render(request, 'envdata/distances/distances.html', context)


def distance(request, pk):
    single_distance = get_object_or_404(DistanceCalculation, id=pk)
    context = {'distance': single_distance}
    return render(request, 'envdata/distances/distance.html', context)


def create_distance(request):
    form = DistanceCalculationForm()
    if request.method == 'POST':
        form = DistanceCalculationForm(request.POST or None)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'envdata/distances/form-distance.html', context)


def update_distance(request, pk):
    updated_distance = get_object_or_404(DistanceCalculation, id=pk)
    form = DistanceCalculationForm(instance=updated_distance)
    if request.method == 'POST':
        form = DistanceCalculationForm(request.POST or None, instance=updated_distance)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'envdata', context)


def delete_distance(request, pk):
    deleted_distance = get_object_or_404(DistanceCalculation, id=pk)
    form = DistanceCalculationForm(instance=deleted_distance)
    if request.method == 'POST':
        deleted_distance.delete()
    context = {'object': form}
    return render(request, 'envdata/delete-universal.html', context)
