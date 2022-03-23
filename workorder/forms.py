from django import forms
from django.forms import ModelForm
from .models import Workorder
from customer.models import Customer


class WorkorderForm(ModelForm):
    organization = forms.ModelChoiceField(queryset=Customer.objects.order_by('name'))

    class Meta:
        model = Workorder
        #fields = ('workorder', 'date', 'organization', 'contact', 'description', 'deadline', 'budget', 'quoted_price')
        fields = ('workorder', 'date', 'organization', 'description', 'deadline', 'budget', 'quoted_price')
        labels = {
            'workorder': '',
            'date': '',
            'organization': '',
            'contact': '',
            'description': '',
            'deadline': '',
            'budget': '',
            'quoted_price': '',
        }
        widgets = {
            'workorder': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Workorder #'}),
            'date': forms.DateInput(attrs={'class':'form-control', 'placeholder':'Date'}),
            'organization': forms.Select(attrs={'class':'form-control', 'placeholder':'Organization'}),
            'contact': forms.Select(attrs={'class':'form-control', 'placeholder':'Contact'}),
            'description': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Description'}),
            'deadline': forms.DateInput(attrs={'class':'form-control', 'placeholder':'Deadline'}),
            'budget': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Budget'}),
            'quoted_price': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Quoted Price'}),
        }
