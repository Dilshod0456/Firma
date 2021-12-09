from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
from .models import Driver, Fikr

User = get_user_model()

class FikirModelForm(forms.ModelForm):
    class Meta:
        model = Fikr
        fields = (
            "kim_tomonidan",
            "discription"         
        )

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

class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}
