from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book  # Associate the form with the Book model
        fields = ['isbn','title', 'author', 'description', 'publisher','page_count','category','lang','publication_date', 'image_url']

    isbn = forms.CharField(label='ISBN', max_length=13)
    title = forms.CharField(label='Title', max_length=100)
    description = forms.CharField(label='Description', widget=forms.Textarea)
    author = forms.CharField(label='Author', max_length=100)
    publisher = forms.CharField(label='Publisher', max_length=100)
    publication_date = forms.CharField(label='Publication Date')
    page_count = forms.IntegerField(label='Page Count')
    category = forms.CharField(label='Category', max_length=100)
    image_url = forms.URLField(label='Image URL')
    lang = forms.CharField(label='Language', max_length=50)

class BookDeleteForm(forms.Form):
    book_id = forms.IntegerField(label='Enter User-Created Book ID to Delete')