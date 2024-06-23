from socialdata.models import HealthAndSafety
from django.forms import ModelForm


class BaseSocialForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(BaseSocialForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


class HealthAndSafetyForm(BaseSocialForm):
    class Meta:
        model = HealthAndSafety
        fields = '__all__'
