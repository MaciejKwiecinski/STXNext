from django.shortcuts import render
from django.http import HttpResponse
from .models import BookInfo, Authors, Identyfires
from django.views import View
import Library.forms as form
import urllib.request
from json import load

api_key = 'AIzaSyAeWfJpdw7Jp6v9yD33EKB31Z3FEkTjg1E'


class BookListView(View):
    def get(self, request):
        dict={}
        books = BookInfo.objects.all()
        authors = Authors.objects.all()
        isbn = Identyfires.objects.all()
        for i in books:
            dict[i]={(authors.filter(book_id=i.id)),(isbn.filter(book_id=i.id))}
        searchform = form.SearchForm
        return render(request, 'booklist.html', {'books': books, 'form': searchform})

    def post(self, request):
        searchform = form.SearchForm(request.POST)
        if searchform.is_valid():
            title = searchform.cleaned_data['title']
            author = searchform.cleaned_data['author']
            language = searchform.cleaned_data['language']
            start = searchform.cleaned_data['dates']
            finish = searchform.cleaned_data['datef']
            books = BookInfo.objects.filter(title__contains=title, authors__name__contains=author,
                                            language__contains=language, publishedDate__range=[start, finish])
        return render(request, 'booklist.html', {'books': books, 'form': searchform})


class AddBookView(View):
    def get(self, request):
        bookform = form.BookInfoForm
        isbnform = form.IdentyfiresForm
        authorform = form.AuthorsForm
        return render(request, 'addbook.html', {'bookform': bookform, 'isbnform': isbnform, 'authorform': authorform})

    def post(self, request):
        books = form.BookInfoForm(request.POST)
        isbn = form.IdentyfiresForm(request.POST)
        author = form.AuthorsForm(request.POST)
        msg = 'Problem with data'
        if books.is_valid() and isbn.is_valid() and author.is_valid():
            b = books.save()
            isbn.save(commit=False)
            author.save(commit=False)
            isbn.book = b
            author.book = b
            msg = 'Done'
        return HttpResponse(msg)


class AddGoogleBookView(View):
    def get(self, request):
        googleform = form.GoogleBookForm
        return render(request, 'googlebook.html', {'form': googleform})

    def post(self, request):
        googleform = form.GoogleBookForm(request.POST)
        msg = 'Done'
        if googleform.is_valid():
            try:
                search_term = googleform.cleaned_data['search_terms']
                url = 'https://www.googleapis.com/books/v1/volumes?q=' + search_term + '&key=' + api_key
                json_obj = urllib.request.urlopen(url)
                data = load(json_obj)
                for i in data['items']:
                    title = i['volumeInfo']['title']
                    publishedDate = i['volumeInfo']['publishedDate']
                    pageCount = i['volumeInfo']['pageCount']
                    imageLinks = i['volumeInfo']['imageLinks']
                    language = i['volumeInfo']['language']
                    book = BookInfo.objects.create(title=title, publishedDate=publishedDate, pageCount=pageCount,
                                                   imageLinks=imageLinks, language=language)
                    for j in i['volumeInfo']['authors']:
                        author = j
                        Authors.objects.create(book=book, name=author)
                    for j in i['volumeInfo']['industryIdentifiers']:
                        type = j['type']
                        num = j['identifier']
                        Identyfires.objects.create(type=type, identifier=num, book=book)
            except:
                msg = 'Problem with data in API'
        return HttpResponse(msg)