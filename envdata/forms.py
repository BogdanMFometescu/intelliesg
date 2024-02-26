from envdata.models import (Company,
                            Fuel,
                            Sf6,
                            Refrigerant,
                            Energy,
                            Travel, Waste)

from django.forms import ModelForm


class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = '__all__'


class FuelForm(ModelForm):
    class Meta:
        model = Fuel
        fields = '__all__'


class Sf6Form(ModelForm):
    class Meta:
        model = Sf6
        fields = '__all__'


class RefrigerantForm(ModelForm):
    class Meta:
        model = Refrigerant
        fields = '__all__'


class EnergyForm(ModelForm):
    class Meta:
        model = Energy
        fields = '__all__'


class TravelForm(ModelForm):
    class Meta:
        model = Travel
        fields = '__all__'


class WasteForm(ModelForm):
    class Meta:
        model = Waste
        fields = '__all__'
