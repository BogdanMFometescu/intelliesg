from socialdata.models import HealthAndSafety, NewEmployeeByAge, EmployeeByContracts, RotationRateOfEmployeeByAge, \
    RetirementRate
from django.forms import ModelForm


class BaseSocialForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(BaseSocialForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

    def save(self, commit=True):
        instance = super(BaseSocialForm, self).save(commit=False)
        if self.user:
            instance.profile = self.user.profile
        if commit:
            instance.save()
        return instance


class HealthAndSafetyForm(BaseSocialForm):
    class Meta:
        model = HealthAndSafety
        fields = '__all__'
        exclude = ['profile']
        labels = {'total_working_hours': 'Total Working Hours',
                  'fatality_rate': 'Fatality Rate',
                  'high_consequence_rate': 'High Consequence Rate',
                  'recordable_rate': 'Recordable Rate',
                  'ep_total_working_hours': 'External Provider Total Working Hours',
                  'ep_fatality_rate': 'External Provider Fatality Rate',
                  'ep_high_consequence_rate': 'External Provider High Consequence Rate',
                  'ep_recordable_rate': 'External Provider Recordable Rate',
                  'total_training_hours': 'Total Training Hours',
                  'management_training_hours': 'Total Training Hours for Management Positions',
                  'operational_training_hours': 'Total Training Hours for Operational Positions',
                  'women_management_training_hours': 'Training Hours for Women with Management Positions',
                  'women_operational_training_hours': 'Training Hours for Women with Operational Positions',
                  'man_management_training_hours': 'Training Hours for Men with Management Positions',
                  'man_operational_training_hours': 'Training Hours for Men with Operational Positions'
                  }


class NewEmployeeByAgeForm(BaseSocialForm):
    class Meta:
        model = NewEmployeeByAge
        fields = '__all__'
        exclude = ['profile']


class EmployeeByContractsForm(BaseSocialForm):
    class Meta:
        model = EmployeeByContracts
        fields = '__all__'
        exclude = ['profile']


class RotationRateOfEmployeeByAgeForm(BaseSocialForm):
    class Meta:
        model = RotationRateOfEmployeeByAge
        fields = '__all__'
        exclude = ['profile']


class RetirementRateForm(BaseSocialForm):
    class Meta:
        model = RetirementRate
        fields = '__all__'
        exclude = ['profile']
