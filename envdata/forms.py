from envdata.models import Emission, FuelEmission

from django.forms import ModelForm


class EmissionForm(ModelForm):
    class Meta:
        model = Emission
        fields = '__all__'
        labels = {'emission_type': 'Emission Type',
                  'emission_scope' : 'Emission Scope'}


class FuelEmissionForm(ModelForm):
    class Meta:
        model = FuelEmission
        fields = '__all__'
