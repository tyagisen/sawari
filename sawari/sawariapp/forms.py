from django import forms
from .models import Driver


class DriverForm(forms.ModelForm):

    class Meta:
        model = Driver
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name', 'id':'name'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone', 'name': 'phone','id':'phone'}),
            'vehicle_type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Vehicle Type', 'name': 'vehicle_type','id':'vechicle'}),
        }