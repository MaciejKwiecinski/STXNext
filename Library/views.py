from django.shortcuts import render
from .models import BookInfo,Identyfires
from django.views import View
from .forms import BookInfoForm,IdentyfiresForm

class BookListView(View):
    def get(self,request):
        books = BookInfo.objects.all()
        form1 = BookInfoForm
        return render(request,'booklist.html',{'books':books,'form1':form1})

    def post(self,request):
        books = BookInfo.objects.filter()