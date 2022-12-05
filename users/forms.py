from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.apps import apps


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': "form-control"
            }),
            'first_name': forms.TextInput(attrs={
                'class': "form-control"
            }),
            'last_name': forms.TextInput(attrs={
                'class': "form-control"
            }),
            'email': forms.EmailInput(attrs={
                'class': "form-control",
                'type': "email"
            }),
            'password1': forms.PasswordInput(attrs={
                'class': "form-control",
                'type': 'password'
            }),
            'password2': forms.PasswordInput(attrs={
                'class': "form-control",
                'type': 'password'
            }),
        }
