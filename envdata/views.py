from django.shortcuts import render

from envdata.forms import EmissionForm, FuelEmissionForm
from envdata.models import Emission, FuelEmission
from django.shortcuts import get_object_or_404


# Create your views here.


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
    context = {'form': form}
    return render(request, 'envdata/form-emission.html', context)


def fuel_emissions(request):
    all_fuel_emissions = FuelEmission.objects.all()
    context = {'fuel_emissions': all_fuel_emissions}
    return render(request, 'envdata/fuel-emissions.html', context)


def fuel_emission(request, pk):
    single_fuel_emission = get_object_or_404(FuelEmission, id=pk)
    context = {'fuel_emission': single_fuel_emission}
    return render(request, 'envdata/single-fuel-emission.html', context)


def create_fuel_emission(request):
    form = FuelEmissionForm()
    if request.method == 'POST':
        form = FuelEmissionForm(request.POST or None)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'envdata/form-fuel-emission.html', context)
