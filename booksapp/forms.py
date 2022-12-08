from django import forms
from .models import Book
from django.forms import ModelForm


class StartBookForm (forms.ModelForm):
    class Meta:
        model = Book
        fields = ['read_status', 'owned', 'date_started']
        widgets = {
            'read_status': forms.Select(attrs={
                'class': "form-control",
                'id': 'inputReadStatus'
            }),
            'owned': forms.CheckboxInput(attrs={
                'class': "form-control form-check-input",
                'id': 'inputOwned'
            }),
            'date_started': forms.NumberInput(attrs={
                'class': "form-control",
                'type': 'date',
                'id': 'inputDateStarted'
            }),
        }


class FinishBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['owned', 'read_status', 'rating', 'notes', 'date_started', 'date_finished', 'times_read']
        widgets = {
            'owned': forms.CheckboxInput(attrs={
                'class': "form-check-input form-control",
                'id': 'inputOwned'
            }),
            'read_status': forms.Select(attrs={
                'class': "form-control",
                'id': 'inputReadStatus'
            }),
            'rating': forms.NumberInput(attrs={
                'class': "form-control",
                'id': 'inputRating'
            }),
            'notes': forms.Textarea(attrs={
                'class': "form-control",
                'rows': 3,
                'id': 'inputNotes'
            }),
            'date_started': forms.NumberInput(attrs={
                'class': "form-control",
                'type': 'date',
                'id': 'inputDateStarted'
            }),
            'date_finished': forms.NumberInput(attrs={
                'class': "form-control",
                'type': 'date',
                'id': 'inputDateFinished'
            }),
            'times_read': forms.NumberInput(attrs={
                'class': "form-control",
                'id': 'inputTimesRead'
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
                'class': "form-control",
                'id': 'inputUser'
            }),
            'title': forms.TextInput(attrs={
                'class': "form-control",
                'id': 'inputTitle'
            }),
            'author': forms.TextInput(attrs={
                'class': "form-control",
                'id': 'inputAuthor'
            }),
            'genre': forms.TextInput(attrs={
                'class': "form-control",
                'id': 'inputGenre'
            }),
            'description': forms.Textarea(attrs={
                'class': "form-control",
                'rows': 3,
                'id': 'inputDescription'
            }),
            'image': forms.FileInput(attrs={
                'class': "form-control-file",
                'id': 'inputImage'
            }),
            'page_count': forms.NumberInput(attrs={
                'class': "form-control",
                'id': 'inputPageCount'
            }),
            'recommended_by': forms.TextInput(attrs={
                'class': "form-control",
                'id': 'inputRecommended'
            }),
            'series_name': forms.TextInput(attrs={
                'class': "form-control",
                'id': 'inputSeriesName'
            }),
            'series_number': forms.NumberInput(attrs={
                'class': "form-control",
                'id': 'inputSeriesNumber'
            }),
            'owned': forms.CheckboxInput(attrs={
                'class': "form-check-input",
                'id': 'inputOwned'
            }),
            'date_added': forms.NumberInput(attrs={
                'class': "form-control",
                'type': 'date',
                'id': 'inputDateAdded'
            }),
            'read_status': forms.Select(attrs={
                'class': "form-control",
                'id': 'inputReadStatus'
            }),
            'rating': forms.NumberInput(attrs={
                'class': "form-control",
                'id': 'inputRating'
            }),
            'notes': forms.Textarea(attrs={
                'class': "form-control",
                'rows': 3,
                'id': 'inputNotes'
            }),
            'date_started': forms.NumberInput(attrs={
                'class': "form-control",
                'type': 'date',
                'id': 'inputDateStarted'
            }),
            'date_finished': forms.NumberInput(attrs={
                'class': "form-control",
                'type': 'date',
                'id': 'inputDateFinished'
            }),
            'times_read': forms.NumberInput(attrs={
                'class': "form-control",
                'id': 'inputTimesRead'
            }),
        }
