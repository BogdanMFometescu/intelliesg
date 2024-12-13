from envdata.models import (
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
                            PurchasedGoodsAndServices,
                            CapitalGoods,
                            FuelEnergyRelatedActivities,
                            UpstreamTransportationAndDistribution,
                            EmployeeCommuting,
                            UpstreamLeasedAssets,
                            DownstreamTransportationAndDistribution,
                            ProcessingOfSoldProducts,
                            UseOfSoldProducts,
                            EndOfLifeTreatmentOfSoldProducts,
                            DownstreamLeasedAssets,
                            Franchises,
                            Investments)

from companies.models import Company
from django.forms import ModelForm
from django import forms
from envdata.constants import *
from common.forms import BaseForm


class CompanyForm(BaseForm):
    class Meta:
        model = Company
        fields = '__all__'
        exclude = ['profile']


class FuelForm(BaseForm):
    class Meta:
        model = Fuel
        fields = '__all__'
        exclude = ['profile']


class Sf6Form(BaseForm):
    class Meta:
        model = Sf6
        fields = '__all__'
        exclude = ['profile']


class RefrigerantForm(BaseForm):
    class Meta:
        model = Refrigerant
        fields = '__all__'
        exclude = ['profile']


class NaturalGasForm(BaseForm):
    class Meta:
        model = NaturalGas
        fields = '__all__'
        exclude = ['profile']


class EnergyForm(BaseForm):
    class Meta:
        model = Energy
        fields = '__all__'
        exclude = ['profile']


class TravelForm(BaseForm):
    class Meta:
        model = Travel
        fields = '__all__'
        exclude = ['profile']


class WasteForm(BaseForm):
    class Meta:
        model = Waste
        fields = '__all__'
        exclude = ['profile']


class TargetForm(BaseForm):
    class Meta:
        model = Target
        fields = '__all__'
        labels = {'co2e_base_year': 'CO2e quantity for base year'}
        exclude = ['profile']


class ExcelUploadForm(forms.Form):
    excel_file = forms.FileField()


class TaxonomySectorForm(BaseForm):
    sector = forms.ChoiceField(choices=TAXONOMY_SECTOR_CHOICES)
    activity = forms.ChoiceField(choices=TAXONOMY_ACTIVITY_CHOICES)

    class Meta:
        model = TaxonomySector
        fields = '__all__'
        exclude = ['profile']


class TaxonomyTurnoverForm(BaseForm):
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


class TaxonomyCapexForm(BaseForm):
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


class TaxonomyOpexForm(BaseForm):
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




class PurchasedGoodsAndServicesForm(BaseForm):
    class Meta:
        model = PurchasedGoodsAndServices
        fields = '__all__'
        exclude = ['profile']


class CapitalGoodsForm(BaseForm):
     class Meta:
        model = CapitalGoods
        fields = '__all__'
        exclude = ['profile']


class FuelEnergyRelatedActivitiesForm(BaseForm):
     class Meta:
        model = FuelEnergyRelatedActivities
        fields = '__all__'
        exclude = ['profile']
    

class UpstreamTransportationAndDistributionForm(BaseForm):
     class Meta:
        model = UpstreamTransportationAndDistribution
        fields = '__all__'
        exclude = ['profile']

class EmployeeCommutingForm(BaseForm):
     class Meta:
        model = EmployeeCommuting
        fields = '__all__'
        exclude = ['profile']


class UpstreamLeasedAssetsForm(BaseForm):
     class Meta:
        model = UpstreamLeasedAssets
        fields = '__all__'
        exclude = ['profile']


class DownstreamTransportationAndDistributionForm(BaseForm):
     class Meta:
        model = DownstreamTransportationAndDistribution
        fields = '__all__'
        exclude = ['profile']


class ProcessingOfSoldProductsForm(BaseForm):
     class Meta:
        model = ProcessingOfSoldProducts
        fields = '__all__'
        exclude = ['profile']


class UseOfSoldProductsForm(BaseForm):
     class Meta:
        model = UseOfSoldProducts
        fields = '__all__'
        exclude = ['profile']


class EndOfLifeTreatmentOfSoldProductsForm(BaseForm):
     class Meta:
        model = EndOfLifeTreatmentOfSoldProducts
        fields = '__all__'
        exclude = ['profile']


class DownstreamLeasedAssetsForm(BaseForm):
     class Meta:
        model = DownstreamLeasedAssets
        fields = '__all__'
        exclude = ['profile']


class FranchisesForm(BaseForm):
     class Meta:
        model = Franchises
        fields = '__all__'
        exclude = ['profile']


class InvestmentsForm(BaseForm):
     class Meta:
        model = Investments
        fields = '__all__'
        exclude = ['profile']

