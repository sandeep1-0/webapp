from django import forms
from crud.models import College


class CollegeForm(forms.ModelForm):
    clg_name=forms.CharField(min_length=3)
    class Meta:
        model=College
        fields='__all__' #bring entire fields from models
        #fields=('clg_name',"clg_email')