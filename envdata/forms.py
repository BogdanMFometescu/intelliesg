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
        exclude = ['owner']

    def __init__(self, *args, **kwargs):
        super(CompanyForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


class BaseProfileForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(BaseProfileForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

    def save(self, commit=True):
        instance = super(BaseProfileForm, self).save(commit=False)
        if self.user:
            instance.profile = self.user.profile
        if commit:
            instance.save()
        return instance


class FuelForm(BaseProfileForm):
    class Meta:
        model = Fuel
        fields = '__all__'
        exclude = ['profile']


class Sf6Form(BaseProfileForm):
    class Meta:
        model = Sf6
        fields = '__all__'
        exclude = ['profile']


class RefrigerantForm(BaseProfileForm):
    class Meta:
        model = Refrigerant
        fields = '__all__'
        exclude = ['profile']


class NaturalGasForm(BaseProfileForm):
    class Meta:
        model = NaturalGas
        fields = '__all__'
        exclude = ['profile']


class EnergyForm(BaseProfileForm):
    class Meta:
        model = Energy
        fields = '__all__'
        exclude = ['profile']


class TravelForm(BaseProfileForm):
    class Meta:
        model = Travel
        fields = '__all__'
        exclude = ['profile']


class WasteForm(BaseProfileForm):
    class Meta:
        model = Waste
        fields = '__all__'
        exclude = ['profile']


class TargetForm(BaseProfileForm):
    class Meta:
        model = Target
        fields = '__all__'
        labels = {'co2e_base_year': 'CO2e quantity for base year'}
        exclude = ['profile']


class ExcelUploadForm(forms.Form):
    excel_file = forms.FileField(label='Upload Excel File')


class TaxonomySectorForm(BaseProfileForm):
    sector = forms.ChoiceField(choices=TAXONOMY_SECTOR_CHOICES)
    activity = forms.ChoiceField(choices=TAXONOMY_ACTIVITY_CHOICES)

    class Meta:
        model = TaxonomySector
        fields = '__all__'
        exclude = ['profile']



class TaxonomyTurnoverForm(BaseProfileForm):
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




class TaxonomyCapexForm(BaseProfileForm):
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




class TaxonomyOpexForm(BaseProfileForm):
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

