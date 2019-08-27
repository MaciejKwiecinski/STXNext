from django.forms import ModelForm
from .models import BookInfo,Identyfires

class BookInfoForm(ModelForm):
    class Meta:
        model = BookInfo
        fields = '__all__'
        exclude = ['industryIdentifiers']

class IdentyfiresForm(ModelForm):
    class Meta:
        model = Identyfires
        fields = '__all__'