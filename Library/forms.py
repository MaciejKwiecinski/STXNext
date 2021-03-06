import django.forms as forms
from .models import BookInfo,Identyfires,Authors

class BookInfoForm(forms.ModelForm):
    class Meta:
        model = BookInfo
        fields = '__all__'

class IdentyfiresForm(forms.ModelForm):
    class Meta:
        model = Identyfires
        fields = '__all__'
        exclude = ['book']

class AuthorsForm(forms.ModelForm):
    class Meta:
        model = Authors
        fields = '__all__'
        exclude = ['book']

class SearchForm(forms.Form):
    title = forms.CharField(label= 'Title',required=None)
    author = forms.CharField(label='Author',required=None)
    language = forms.CharField(label='Language',required=None)

class GoogleBookForm(forms.Form):
    search_terms = forms.CharField(label= 'Search item', required=True)