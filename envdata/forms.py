from envdata.models import Emission, FuelEmission

from django.forms import ModelForm


class EmissionForm(ModelForm):
    class Meta:
        model = Emission
        fields = '__all__'


class FuelEmissionForm(ModelForm):
    class Meta:
        model = FuelEmission
        fields = '__all__'
