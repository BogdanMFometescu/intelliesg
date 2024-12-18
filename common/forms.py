
from django.forms import ModelForm

class BaseForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(BaseForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

    def save(self, commit=True):
        instance = super(BaseForm, self).save(commit=False)
        if self.user:
            instance.profile = self.user.profile
        if commit:
            instance.save()
        return instance