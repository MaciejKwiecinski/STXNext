from django.shortcuts import render,redirect
from .models import BookInfo
from django.core.exceptions import ValidationError
from django.views import View
import Library.forms as form

class BookListView(View):
    def get(self,request):
        books = BookInfo.objects.all()
        searchform = form.SearchForm
        return render(request,'booklist.html',{'books':books,'form':searchform})

    def post(self,request):
        searchform = form.SearchForm(request.POST)
        if searchform.is_valid():
            title = searchform.cleaned_data['title']
            author = searchform.cleaned_data['author']
            language = searchform.cleaned_data['language']
            start = searchform.cleaned_data['dates']
            finish = searchform.cleaned_data['datef']
            books = BookInfo.objects.filter(title__contains =  title, authors__name__contains= author, language__contains = language, publishedDate__range=[start,finish])
        return render(request,'booklist.html',{'books':books,'form':searchform})

class AddBookView(View):
    def get(self,request):
        bookform = form.BookInfoForm
        isbnform = form.IdentyfiresForm
        authorform = form.AuthorsForm
        return render(request,'addbook.html',{'bookform':bookform,'isbnform':isbnform,'authorform':authorform})


    def post(self,request):
        book = form.BookInfoForm(request.POST)
        isbn = form.IdentyfiresForm(request.POST)
        author = form.AuthorsForm(request.POST)
        if isbn.is_valid() and author.is_valid() and book.is_valid():
            num = isbn.save()
            auth = author.save()
            book = book.save(commit=False)
            book.industryIdentifiers = num
            book.authors = auth
            book.save()
        return redirect('/books')

