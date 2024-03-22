from envdata.models import (Company,
                            Fuel,
                            Sf6,
                            Refrigerant,
                            NaturalGas,
                            Energy,
                            Travel,
                            Waste,
                            Target)

from django.forms import ModelForm


class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = '__all__'
        exclude = ['owner']

    def __init__(self, *args, **kwargs):
        super(CompanyForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


class FuelForm(ModelForm):
    class Meta:
        model = Fuel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(FuelForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


class Sf6Form(ModelForm):
    class Meta:
        model = Sf6
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(Sf6Form, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


class RefrigerantForm(ModelForm):
    class Meta:
        model = Refrigerant
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(RefrigerantForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


class NaturalGasForm(ModelForm):
    class Meta:
        model = NaturalGas
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(NaturalGasForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


class EnergyForm(ModelForm):
    class Meta:
        model = Energy
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EnergyForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


class TravelForm(ModelForm):
    class Meta:
        model = Travel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(TravelForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


class WasteForm(ModelForm):
    class Meta:
        model = Waste
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(WasteForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


class TargetForm(ModelForm):
    class Meta:
        model = Target
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(TargetForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
