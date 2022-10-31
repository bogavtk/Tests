from django import forms
from .models import Calc_History


class AppForm(forms.ModelForm):
    def save(self, *args, **kwargs):
        self.instance.result = self.initial['result']
        return super(AppForm, self).save(*args, **kwargs)

    class Meta:
        model = Calc_History
        fields = ['val1', 'val2', 'operator']
