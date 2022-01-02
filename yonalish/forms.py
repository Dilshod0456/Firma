from django import forms
from django.forms import fields
from driver.models import Yonalish


class YonalishModelForms(forms.ModelForm):
    class Meta:
        model = Yonalish
        fields = (
            'user',
            'organisation',
        )