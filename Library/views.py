from django.shortcuts import render,redirect
from .models import BookInfo
from django.core.exceptions import ValidationError
from django.views import View
from .forms import BookInfoForm,IdentyfiresForm,AuthorsForm

class BookListView(View):
    def get(self,request):
        books = BookInfo.objects.all()
        return render(request,'booklist.html',{'books':books})

    def post(self,request):

        books = BookInfo.objects.filter()
        return render(request,'booklist.html',{'books':books})

class AddBookView(View):
    def get(self,request):
        bookform = BookInfoForm
        isbnform = IdentyfiresForm
        authorform = AuthorsForm
        return render(request,'addbook.html',{'bookform':bookform,'isbnform':isbnform,'authorform':authorform})

    def post(self,request):
        book = BookInfoForm(request.POST)
        isbn = IdentyfiresForm(request.POST)
        author = AuthorsForm(request.POST)
        if isbn.is_valid() and author.is_valid() and book.is_valid():
            num = isbn.save()
            auth = author.save()
            book = book.save(commit=False)
            book.industryIdentifiers = num
            book.authors = auth
            book.save()
        else:
            raise ValidationError ('Wrong value')
        return redirect('/books')
