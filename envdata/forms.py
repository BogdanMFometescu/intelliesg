from envdata.models import (Company,
                            Fuel,
                            Sf6,
                            Refrigerant,
                            NaturalGas,
                            Energy,
                            Travel,
                            Waste,
                            Target,
                            TaxonomyTurnover,
                            TaxonomySector,
                            TaxonomyOpEx,
                            TaxonomyCapEx,
                            )

from django.forms import ModelForm
from django import forms
from envdata.constants import *


class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = '__all__'
        exclude = ['owner','profile']

    def __init__(self, *args, **kwargs):
        super(CompanyForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


class FuelForm(ModelForm):
    class Meta:
        model = Fuel
        fields = '__all__'
        exclude = ['profile']

    def __init__(self, *args, **kwargs):
        super(FuelForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


class Sf6Form(ModelForm):
    class Meta:
        model = Sf6
        fields = '__all__'
        exclude = ['profile']

    def __init__(self, *args, **kwargs):
        super(Sf6Form, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


class RefrigerantForm(ModelForm):
    class Meta:
        model = Refrigerant
        fields = '__all__'
        exclude = ['profile']

    def __init__(self, *args, **kwargs):
        super(RefrigerantForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


class NaturalGasForm(ModelForm):
    class Meta:
        model = NaturalGas
        fields = '__all__'
        exclude = ['profile']

    def __init__(self, *args, **kwargs):
        super(NaturalGasForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


class EnergyForm(ModelForm):
    class Meta:
        model = Energy
        fields = '__all__'
        exclude = ['profile']

    def __init__(self, *args, **kwargs):
        super(EnergyForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


class TravelForm(ModelForm):
    class Meta:
        model = Travel
        fields = '__all__'
        exclude = ['profile']

    def __init__(self, *args, **kwargs):
        super(TravelForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


class WasteForm(ModelForm):
    class Meta:
        model = Waste
        fields = '__all__'
        exclude = ['profile']

    def __init__(self, *args, **kwargs):
        super(WasteForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


class TargetForm(ModelForm):
    class Meta:
        model = Target
        fields = '__all__'
        labels = {'co2e_base_year': 'CO2e quantity for base year'}
        exclude = ['profile']

    def __init__(self, *args, **kwargs):
        super(TargetForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


class ExcelUploadForm(forms.Form):
    excel_file = forms.FileField(label='Upload Excel File')


class TaxonomySectorForm(ModelForm):
    sector = forms.ChoiceField(choices=TAXONOMY_SECTOR_CHOICES)
    activity = forms.ChoiceField(choices=TAXONOMY_ACTIVITY_CHOICES)

    class Meta:
        model = TaxonomySector
        fields = '__all__'
        exclude = ['profile']

    def __init__(self, *args, **kwargs):
        super(TaxonomySectorForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


class TaxonomyTurnoverForm(ModelForm):
    class Meta:
        model = TaxonomyTurnover
        fields = '__all__'
        labels = {'turnover_activity': 'Activity',
                  'total_turnover': 'Indicate your total turnover of the last financial period',
                  'turnover_eligible': 'Eligible turnover amount',
                  'turnover_aligned': 'Aligned turnover amount',
                  'turnover_non_eligible': 'Non-Eligible turnover amount',
                  'climate_change_adaptation': 'To what percentage does your activity fit with the substantial contribution criteria for climate change adaptation?',
                  'climate_change_mitigation': 'To what percentage does your activity fit with the substantial contribution criteria for climate change mitigation?',
                  'climate_change_dnsh': 'Do your activities comply with the DNSH criteria for climate change?',
                  'marine_resources_dnsh': 'Do your activities comply with the DNSH criteria for marine resources?',
                  'circular_economy_dnsh': 'Do your activities comply with the DNSH criteria for circular economy?',
                  'pollution_dnsh': 'Do your activities comply with the DNSH criteria for pollution?',
                  'biodiversity_dnsh': 'Do your activities comply with the DNSH criteria for biodiversity?'
                  }
        exclude = ['profile']

    def __init__(self, *args, **kwargs):
        super(TaxonomyTurnoverForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


class TaxonomyCapexForm(ModelForm):
    class Meta:
        model = TaxonomyCapEx
        fields = '__all__'
        labels = {'capex_activity': 'Activity',
                  'capex_turnover': 'Indicate your total CapEx of the last financial period',
                  'capex_eligible': 'Eligible CapEx amount',
                  'capex_aligned': 'Aligned CapEx amount',
                  'capex_non_eligible': 'Non-Eligible CapEx amount',
                  'climate_change_dnsh': 'Do your activities comply with the DNSH criteria for climate change?',
                  'marine_resources_dnsh': 'Do your activities comply with the DNSH criteria for marine resources?',
                  'circular_economy_dnsh': 'Do your activities comply with the DNSH criteria for circular economy?',
                  'pollution_dnsh': 'Do your activities comply with the DNSH criteria for pollution?',
                  'biodiversity_dnsh': 'Do your activities comply with the DNSH criteria for biodiversity?'
                  }
        exclude = ['profile']

    def __init__(self, *args, **kwargs):
        super(TaxonomyCapexForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


class TaxonomyOpexForm(ModelForm):
    class Meta:
        model = TaxonomyOpEx
        fields = '__all__'
        labels = {'opex_activity': 'Activity',
                  'opex_turnover': 'Indicate your total OpEx of the last financial period',
                  'opex_eligible': 'Eligible OpEx amount',
                  'opex_aligned': 'Aligned OpEx amount',
                  'opex_non_eligible': 'Non-Eligible OpEx amount',
                  'climate_change_dnsh': 'Do your activities comply with the DNSH criteria for climate change?',
                  'marine_resources_dnsh': 'Do your activities comply with the DNSH criteria for marine resources?',
                  'circular_economy_dnsh': 'Do your activities comply with the DNSH criteria for circular economy?',
                  'pollution_dnsh': 'Do your activities comply with the DNSH criteria for pollution?',
                  'biodiversity_dnsh': 'Do your activities comply with the DNSH criteria for biodiversity?'
                  }
        exclude = ['profile']

    def __init__(self, *args, **kwargs):
        super(TaxonomyOpexForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
