import django.forms as forms
from .models import BookInfo,Identyfires,Authors

class BookInfoForm(forms.ModelForm):
    class Meta:
        model = BookInfo
        exclude = ['industryIdentifiers','authors']

class IdentyfiresForm(forms.ModelForm):
    class Meta:
        model = Identyfires
        fields = '__all__'

class AuthorsForm(forms.ModelForm):
    class Meta:
        model = Authors
        fields = '__all__'

class SearchForm(forms.Form):
    title = forms.CharField(label= 'Title',required=None)
    author = forms.CharField(label='Author',required=None)
    language = forms.CharField(label='Language',required=None)
    dates = forms.CharField(label='Start',required=None,empty_value=0)
    datef = forms.CharField(label='Finish',required=None, empty_value=2019)
