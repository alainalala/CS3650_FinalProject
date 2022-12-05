from django import forms
from .models import Book
from django.forms import ModelForm


class StartBookForm (forms.ModelForm):
    class Meta:
        model = Book
        fields = ['read_status', 'owned', 'date_started']
        widgets = {
            'read_status': forms.Select(attrs={
                'class': "form-control"
            }),
            'owned': forms.CheckboxInput(attrs={
                'class': "form-control form-check-input"
            }),
            'date_started': forms.NumberInput(attrs={
                'class': "form-control",
                'type': 'date'
            }),
        }


class FinishBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['owned', 'read_status', 'rating', 'notes', 'date_started', 'date_finished', 'times_read']
        widgets = {
            'owned': forms.CheckboxInput(attrs={
                'class': "form-check-input form-control",
            }),
            'read_status': forms.Select(attrs={
                'class': "form-control"
            }),
            'rating': forms.NumberInput(attrs={
                'class': "form-control"
            }),
            'notes': forms.Textarea(attrs={
                'class': "form-control",
                'rows': 3
            }),
            'date_started': forms.NumberInput(attrs={
                'class': "form-control",
                'type': 'date'
            }),
            'date_finished': forms.NumberInput(attrs={
                'class': "form-control",
                'type': 'date'
            }),
            'times_read': forms.NumberInput(attrs={
                'class': "form-control"
            }),
        }


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['user', 'title', 'author', 'genre', 'description', 'image', 'page_count', 'recommended_by',
                  'series_name', 'series_number', 'owned', 'date_added', 'read_status', 'rating', 'notes',
                  'date_started', 'date_finished', 'times_read']
        widgets = {
            'user': forms.Select(attrs={
                'class': "form-control"
            }),
            'title': forms.TextInput(attrs={
                'class': "form-control"
            }),
            'author': forms.TextInput(attrs={
                'class': "form-control"
            }),
            'genre': forms.TextInput(attrs={
                'class': "form-control"
            }),
            'description': forms.Textarea(attrs={
                'class': "form-control",
                'rows': 3
            }),
            'image': forms.FileInput(attrs={
                'class': "form-control-file"
            }),
            'page_count': forms.NumberInput(attrs={
                'class': "form-control"
            }),
            'recommended_by': forms.TextInput(attrs={
                'class': "form-control"
            }),
            'series_name': forms.TextInput(attrs={
                'class': "form-control"
            }),
            'series_number': forms.NumberInput(attrs={
                'class': "form-control"
            }),
            'owned': forms.CheckboxInput(attrs={
                'class': "form-check-input"
            }),
            'date_added': forms.NumberInput(attrs={
                'class': "form-control",
                'type': 'date'
            }),
            'read_status': forms.Select(attrs={
                'class': "form-control"
            }),
            'rating': forms.NumberInput(attrs={
                'class': "form-control"
            }),
            'notes': forms.Textarea(attrs={
                'class': "form-control",
                'rows': 3
            }),
            'date_started': forms.NumberInput(attrs={
                'class': "form-control",
                'type': 'date'
            }),
            'date_finished': forms.NumberInput(attrs={
                'class': "form-control",
                'type': 'date'
            }),
            'times_read': forms.NumberInput(attrs={
                'class': "form-control"
            }),
        }
