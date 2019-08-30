from django.shortcuts import render
from django.http import HttpResponse
from .models import BookInfo, Authors, Identyfires
from django.views import View
import Library.forms as form
import urllib.request
from json import load

api_key = 'AIzaSyAeWfJpdw7Jp6v9yD33EKB31Z3FEkTjg1E'

def main(request):
    return render(request,'main.html')

class BookListView(View):
    def get(self, request):
        books = BookInfo.objects.all()
        authors = Authors.objects.all().prefetch_related('book__identyfires_set')
        isbn = Identyfires.objects.all().prefetch_related('book__authors_set')
        searchform = form.SearchForm
        return render(request, 'booklist.html', {'books': books,'author':authors , 'isbn':isbn , 'form': searchform})

    def post(self, request):
        searchform = form.SearchForm(request.POST)
        if searchform.is_valid():
            title = searchform.cleaned_data['title']
            author = searchform.cleaned_data['author']
            language = searchform.cleaned_data['language']
            books = BookInfo.objects.filter(title__contains=title, authors__name__contains=author,
                                            language__contains=language )
        return render(request, 'booklist.html', {'books': books, 'form': searchform})


class AddBookView(View):
    def get(self, request):
        bookform = form.BookInfoForm
        isbnform = form.IdentyfiresForm
        authorform = form.AuthorsForm
        return render(request, 'addbook.html', {'bookform': bookform, 'isbnform': isbnform, 'authorform': authorform})

    def post(self, request):
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
                        typ = j['type']
                        num = j['identifier']
                        Identyfires.objects.create(type=typ, identifier=num, book=book)
        return HttpResponse(msg)