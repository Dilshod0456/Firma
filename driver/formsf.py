from django import forms
class FikrForm(forms.Form):
    kim_tomonidan = forms.CharField(max_length=50)
    discription = forms.CharField(widget=forms.Textarea)
