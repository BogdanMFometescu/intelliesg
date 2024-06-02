from django.forms import ModelForm
from esgmanager.models import ESGPillars, ESGActionPlan, ESGActionPlanObjectives, ESGActionPlanActions, \
    NetZeroBusinessPlan, EnvironmentalRisk, ClimateChangeRisk, SocialRisk, GovernanceRisks


class ESGPillarsForm(ModelForm):
    class Meta:
        model = ESGPillars
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ESGPillarsForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


class ESGActionPlanForm(ModelForm):
    class Meta:
        model = ESGActionPlan
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ESGActionPlanForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


class ESGActionPlanObjectivesForm(ModelForm):
    class Meta:
        model = ESGActionPlanObjectives
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ESGActionPlanObjectivesForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


class ESGActionPlanActionsForm(ModelForm):
    class Meta:
        model = ESGActionPlanActions
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ESGActionPlanActionsForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


class NetZeroBusinessPlanForm(ModelForm):
    class Meta:
        model = NetZeroBusinessPlan
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(NetZeroBusinessPlanForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


class EnvironmentalRisksForm(ModelForm):
    class Meta:
        model = EnvironmentalRisk
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EnvironmentalRisksForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


class ClimateChangeRisksForm(ModelForm):
    class Meta:
        model = ClimateChangeRisk
        fields = '__all__'
        labels = {'cc_category': 'Category',
                  'cc_risk': 'Risk',
                  'cc_description': 'Description',
                  'cc_probability': 'Probability',
                  'cc_mitigation_measures': 'Mitigation Measures',
                  'cc_opportunities': 'Opportunities',
                  'cc_severity': 'Severity',
                  'cc_responsible': 'Responsible'}

    def __init__(self, *args, **kwargs):
        super(ClimateChangeRisksForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


class SocialRisksForm(ModelForm):
    class Meta:
        model = SocialRisk
        fields = '__all__'
        labels = {'soc_category': 'Category',
                  'soc_risk': 'Risk',
                  'soc_description': 'Description',
                  'soc_probability': 'Probability',
                  'soc_mitigation_measures': 'Mitigation Measures',
                  'soc_opportunities': 'Opportunities',
                  'soc_severity': 'Severity',
                  'soc_responsible': 'Responsible'}


    def __init__(self, *args, **kwargs):
        super(SocialRisksForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


class GovernanceRisksForm(ModelForm):
    class Meta:
        model = GovernanceRisks
        fields = '__all__'
        labels = {'gov_category': 'Category',
                  'gov_risk': 'Risk',
                  'gov_description': 'Description',
                  'gov_probability': 'Probability',
                  'gov_mitigation_measures': 'Mitigation Measures',
                  'gov_opportunities': 'Opportunities',
                  'gov_severity': 'Severity',
                  'gov_responsible': 'Responsible'}

    def __init__(self, *args, **kwargs):
        super(GovernanceRisksForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
