from django.forms import ModelForm
from esgmanager.models import ESGPillars, ESGActionPlan, ESGActionPlanObjectives, ESGActionPlanActions, \
    NetZeroBusinessPlan, EnvironmentalRisk, ClimateChangeRisk, SocialRisk, GovernanceRisks, ESGStrategy


class BaseEsGManagerForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(BaseEsGManagerForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


class ESGPillarsForm(BaseEsGManagerForm):
    class Meta:
        model = ESGPillars
        fields = '__all__'


class ESGActionPlanForm(BaseEsGManagerForm):
    class Meta:
        model = ESGActionPlan
        fields = '__all__'


class ESGActionPlanObjectivesForm(BaseEsGManagerForm):
    class Meta:
        model = ESGActionPlanObjectives
        fields = '__all__'


class ESGActionPlanActionsForm(BaseEsGManagerForm):
    class Meta:
        model = ESGActionPlanActions
        fields = '__all__'


class NetZeroBusinessPlanForm(BaseEsGManagerForm):
    class Meta:
        model = NetZeroBusinessPlan
        fields = '__all__'


class EnvironmentalRisksForm(BaseEsGManagerForm):
    class Meta:
        model = EnvironmentalRisk
        fields = '__all__'


class ClimateChangeRisksForm(BaseEsGManagerForm):
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


class SocialRisksForm(BaseEsGManagerForm):
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


class GovernanceRisksForm(BaseEsGManagerForm):
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


class StrategyForm(BaseEsGManagerForm):
    class Meta:
        model = ESGStrategy
        fields = '__all__'
        labels = {'introduction': 'Describe how you defined your ESG Strategy',
                  'pillar_description': 'Describe how you defined your ESG Pillars',
                  'objectives_description': 'Describe how you set your ESG Objectives',
                  'action_plan_description': 'Describe how you set your ESG Action Plan',
                  'actions_description': 'Describe how you defined your ESG actions',
                  'risks_description': 'Describe how you defined your ESG risks'}
