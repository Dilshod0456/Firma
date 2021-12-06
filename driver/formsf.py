"""from django import forms
class FikrForm(forms.Form):
    kim_tomonidan = forms.CharField(max_length=50)
    discription = forms.CharField(widget=forms.Textarea)

"""
from django import forms
from .models import  Fikr

class FikirModelForm(forms.ModelForm):
    class Meta:
        model = Fikr
        fields = (
            "kim_tomonidan",
            "discription"         
        )
