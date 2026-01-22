from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    published_date = forms.DateField(
        input_formats=['%d/%m/%Y'],
        widget=forms.DateInput(
            attrs={
                'placeholder': 'DD/MM/YYYY',
                'class': 'form-control'
            }
        )
    )

    class Meta:
        model = Book
        fields = ['title', 'author', 'description', 'published_date']
