from common.forms import BaseForm
from .models import Company

class CompanyForm(BaseForm):
    class Meta:
        model = Company
        fields = '__all__'
        exclude = ['profile']
