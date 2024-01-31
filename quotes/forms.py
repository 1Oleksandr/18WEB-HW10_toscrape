from django.forms import ModelForm, CharField, TextInput
from .models import Author, Tag, Quote

class QATForm(ModelForm):
    quote = CharField(required=True, widget=TextInput(
        attrs={'class': 'form-control'}))
    fullname = CharField(max_length=50, required=True, widget=TextInput(
        attrs={'class': 'form-control'}))
    born_date = CharField(max_length=50, widget=TextInput(
        attrs={'class': 'form-control'}))
    born_location = CharField(max_length=100, widget=TextInput(
        attrs={'class': 'form-control'}))
    description = CharField(widget=TextInput(
        attrs={'class': 'form-control'}))
    name = CharField(max_length=50, widget=TextInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = Quote
        fields = ('quote',)

        model = Author
        fields = ('fullname', 'born_date', 'born_location', 'description')

        model = Tag
        fields = ('name',)