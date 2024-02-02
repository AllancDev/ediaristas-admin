from django import forms
from ..models import Service
from django.forms import widgets
from decimal import Decimal


class ServiceForm(forms.ModelForm):
    minimum_value = forms.CharField(widget=forms.TextInput(attrs={'class': 'money'}))
    commission_percentage = forms.CharField(widget=forms.TextInput(attrs={'class': 'money'}))
    hall_value = forms.CharField(widget=forms.TextInput(attrs={'class': 'money'}))
    bathroom_value = forms.CharField(widget=forms.TextInput(attrs={'class': 'money'}))
    kitchen_value = forms.CharField(widget=forms.TextInput(attrs={'class': 'money'}))
    others_value = forms.CharField(widget=forms.TextInput(attrs={'class': 'money'}))

    class Meta:
        model = Service
        fields = '__all__'

    def clean_minimum_value(self):
        data = self.cleaned_data['minimum_value']
        return Decimal(data.replace(',', '.'))

    def clean_commission_percentage(self):
        data = self.cleaned_data['commission_percentage']
        return Decimal(data.replace(',', '.'))

    def clean_hall_value(self):
        data = self.cleaned_data['hall_value']
        return Decimal(data.replace(',', '.'))

    def clean_bathroom_value(self):
        data = self.cleaned_data['bathroom_value']
        return Decimal(data.replace(',', '.'))

    def clean_kitchen_value(self):
        data = self.cleaned_data['kitchen_value']
        return Decimal(data.replace(',', '.'))
    
    def clean_others_value(self):
        data = self.cleaned_data['others_value']
        return Decimal(data.replace(',', '.'))