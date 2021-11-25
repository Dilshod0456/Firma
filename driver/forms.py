from django import forms
from django.db.models import fields
from .models import Driver

class DriverModelForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = (
            "Ismi",
            "Familyasi",
            "Yoshi",
            "Staji",
            "Yonalish"            
        )

class DriverForm(forms.Form):
    Ismi = forms.CharField(max_length=20)
    Familyasi = forms.CharField(max_length=20)
    Yoshi = forms.IntegerField(min_value=0)
    Staji = forms.IntegerField(min_value=0)