from django.forms import ModelForm,Form
from .models import BookInfo,Identyfires,Authors

class BookInfoForm(ModelForm):
    class Meta:
        model = BookInfo
        exclude = ['industryIdentifiers','authors']

class IdentyfiresForm(ModelForm):
    class Meta:
        model = Identyfires
        fields = '__all__'

class AuthorsForm(ModelForm):
    class Meta:
        model = Authors
        fields = '__all__'

class TitleSearchForm(Form):

class AuthorSearchForm(Form):

class LanguageSearchForm(Form):

class PublishedDateSearchForm(Form):
