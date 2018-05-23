from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from eggfarm.models import Orders, Capacity, Prices
from django.core.exceptions import ValidationError
from django.core import validators
from django.utils import timezone


class ClientRegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=20, label='Username')
    address = forms.CharField(max_length=30, label='Place of Residence')
    contact_number = forms.IntegerField(label='enter valid phone number')
    NIN = forms.CharField(max_length=15, label='National I.D Number', widget=forms.TextInput(attrs={'class': 'input'}))

    class Meta:
        model = User
        fields = ['username', 'address', 'contact_number', 'NIN']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'input', 'required': True}),
            'address': forms.TextInput(attrs={'class': 'input', 'required': True}),
            'contact_number': forms.NumberInput(attrs={'class': 'input', 'required': True}),
            'NIN': forms.TextInput(attrs={'class': 'input', 'required': True})

        }


class LoginForm(forms.Form):
    username = UsernameField(
        widget=forms.TextInput(attrs={'class': 'input', 'autofocus': True, 'placeholder': 'username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'password'}))

    class Meta:
        model = User


class BookingForm(forms.ModelForm):
    no_of_trays = forms.IntegerField(label='Number of trays desired')
    location = forms.CharField(max_length=30, label='Where You Are Located')

    class Meta:
        model = Orders
        fields = ['no_of_trays', 'location']
        widgets = {
            'no_of_trays': forms.NumberInput(attrs={'class': 'input', 'required': True}),
            'location': forms.TextInput(attrs={'class': 'input', 'required': True})
        }