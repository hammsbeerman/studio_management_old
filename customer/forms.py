from django import forms
from django.forms import ModelForm
from .models import Customer, Contact


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'address1', 'address2', 'city', 'state', 'zipcode', 'phone1', 'phone2', 'email', 'website',]
        labels = {
            'name': '',
            'address1': '',
            'address2': '',
            'city': '',
            'state': '',
            'zipcode': '',
            'phone1': '',
            'phone2': '',
            'email': '',
            'website': '',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Customer Name'}),
            'address1': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address 1'}),
            'address2': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address 2'}),
            'city': forms.TextInput(attrs={'class':'form-control', 'placeholder':'City'}),
            'state': forms.TextInput(attrs={'class':'form-control', 'placeholder':'State'}),
            'zipcode': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Zipcode'}),
            'phone1': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone 1'}),
            'phone2': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone 2'}),
            'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}),
            'website': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Website'}),
        }



class CustomerContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['customer', 'fname', 'lname', 'phone1', 'email',]
        labels = {
            'customer':'',
            'fname':'Contact First Name',
            'lname':'Contact Last Name',
            'phone1':'',
            'email':'',
        }
        widgets = {
            'customer': forms.Select(attrs={'class':'form-control', 'placeholder':'Organization'}),
            'fname': forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}),
            'lname': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}),
            'phone1': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone Number'}),
            'email': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email'}),
        }

class SingleCustomerContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['fname', 'lname', 'phone1', 'email',]
        labels = {
            'fname':'Contact First Name',
            'lname':'Contact Last Name',
            'phone1':'',
            'email':'',
        }
        widgets = {
            'fname': forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}),
            'lname': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}),
            'phone1': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone Number'}),
            'email': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email'}),
        }
