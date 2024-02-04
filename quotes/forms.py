from django.forms import ModelForm, ModelChoiceField, CharField, TextInput, Textarea, IntegerField, Select
from .models import Author, Tag, Quote

class QuoteForm(ModelForm):
    quote = CharField(required=True, widget=TextInput(
        attrs={'class': 'form-control'}))
    # authors = Author.objects.all()
    # authors = Author.objects.values_list('id','fullname')
    author = ModelChoiceField(queryset = Author.objects.all(), widget=Select(
        attrs={'class': 'form-control'}))

    class Meta:
        model = Quote
        fields = ('quote', 'author')

class AuthorForm(ModelForm):
    fullname = CharField(max_length=50, required=True, widget=TextInput(
        attrs={'class': 'form-control'}))
    born_date = CharField(max_length=50, widget=TextInput(
        attrs={'class': 'form-control'}))
    born_location = CharField(max_length=100, widget=TextInput(
        attrs={'class': 'form-control'}))
    description = CharField(widget=Textarea(
        attrs={'class': 'form-control'}))
    
    class Meta:
        model = Author
        fields = ('fullname', 'born_date', 'born_location', 'description')


class TagForm(ModelForm):
    name = CharField(max_length=50, widget=TextInput(
        attrs={'class': 'form-control'}))
    
    class Meta:
        model = Tag
        fields = ('name',)