from envdata.models import (Emission,
                            FuelEmission,
                            Sf6Emission,
                            RefrigerantEmission,
                            EnergyAcquisition, Travel)

from django.forms import ModelForm


class EmissionForm(ModelForm):
    class Meta:
        model = Emission
        fields = '__all__'
        labels = {'emission_type': 'Emission Type',
                  'emission_scope': 'Emission Scope'}


class FuelEmissionForm(ModelForm):
    class Meta:
        model = FuelEmission
        fields = '__all__'


class Sf6EmissionForm(ModelForm):
    class Meta:
        model = Sf6Emission
        fields = '__all__'


class RefrigerantEmissionForm(ModelForm):
    class Meta:
        model = RefrigerantEmission
        fields = '__all__'


class EnergyAcquisitionForm(ModelForm):
    class Meta:
        model = EnergyAcquisition
        fields = '__all__'


class TravelForm(ModelForm):
    class Meta:
        model = Travel
        fields = '__all__'
