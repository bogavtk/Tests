from django import forms
from .models import Calc_History


class AppForm(forms.ModelForm):
    val1 = forms.IntegerField()
    val2 = forms.IntegerField()
    operator = forms.CharField(max_length=10)

    class Meta:
        model = Calc_History
        fields = ['val1', 'val2', 'operator']
