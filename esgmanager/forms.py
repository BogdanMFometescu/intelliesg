from django.forms import ModelForm
from esgmanager.models import ESGPillars, ESGActionPlan, ESGActionPlanObjectives, ESGActionPlanActions, \
    NetZeroBusinessPlan


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
