from django import forms
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
