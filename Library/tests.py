from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse,resolve
from .views import BookListView, main
from .api.views import DocsView,BooksApiView
from Library.models import BookInfo,Authors,Identyfires
from Library.forms import BookInfoForm,SearchForm
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse as api_reverse
from rest_framework import status
# I think if i will show you test of every part, it will be enough.

class TestUrls(SimpleTestCase):
    def test_booklist(self):
        url = reverse('booklist')
        self.assertEquals(resolve(url).func.view_class,BookListView)

    def test_apilist(self):
        url = reverse('apilist')
        self.assertEquals(resolve(url).func.view_class,DocsView)

    def test_apibooklist(self):
        url = reverse('apibooklist')
        self.assertEquals(resolve(url).func.view_class, BooksApiView)

    def test_main(self):
        url = reverse('main')
        self.assertEquals(resolve(url).func, main)

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()

    def test_AddBookGET(self):
        response = self.client.get(reverse(('addbook')))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'addbook.html')

    def test_AddBookPOST(self):
        response = self.client.post(reverse('addbook'),{
            'title':'Hobbit',
            'publishedDate':'1986',
            'pageCount':'123',
            'imageLinks':'whatever',
            'language':'en',
            'name':'J.R.R. Tolkien',
            'type':'ISBN-13',
            'identyfire':'123456781',
        })

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'message.html')

class TestModels(TestCase):

    def setUp(self):
        self.book1 = BookInfo.objects.create(
        title = 'Hobbit',
        publishedDate = '1986',
        pageCount = '123',
        imageLinks = 'whatever',
        language = 'en',
        )
        self.author1 = Authors.objects.create(
            name = 'J.R.R. Tolkien',
            book = self.book1
        )
        self.isbn1 = Identyfires.objects.create(
            type = 'ISBN-13',
            identifier = '123456754123X',
            book = self.book1
        )

    def test_all_book_info(self):

        self.assertEquals(self.book1.title, 'Hobbit')
        self.assertEquals(self.author1.name, 'J.R.R. Tolkien')
        self.assertEquals(self.author1.book.title, 'Hobbit')
        self.assertEquals(self.author1.book.publishedDate, '1986')
        self.assertEquals(self.author1.book.pageCount, '123')
        self.assertEquals(self.author1.book.imageLinks, 'whatever')
        self.assertEquals(self.author1.book.language, 'en')
        self.assertEquals(self.isbn1.book.title, 'Hobbit')
        self.assertEquals(self.isbn1.book.pageCount, '123')
        self.assertEquals(self.isbn1.book.publishedDate, '1986')
        self.assertEquals(self.isbn1.book.imageLinks, 'whatever')
        self.assertEquals(self.isbn1.book.language, 'en')
        self.assertEquals(self.isbn1.type, 'ISBN-13')
        self.assertEquals(self.isbn1.identifier, '123456754123X')

class TestForms(SimpleTestCase):
    def test_BookInfoForm(self):
        form = BookInfoForm(data={
            'title':'Hobbit',
            'publishedDate':'1986',
            'pageCount':'123',
            'imageLinks':'whatever',
            'language':'en',
        })
        self.assertTrue(form.is_valid())

    def test_SearchForm(self):
        form = SearchForm(data={
            'title': 'Whatever',
            'author': 'J.R.R. Tolkien',
            'language': 'pl'
        })

        self.assertTrue(form.is_valid())

        form = SearchForm()

        self.assertFalse(form.is_valid())

        form = SearchForm(data = {
            'title':'Whatever'
        })

        self.assertTrue(form.is_valid())

class TestAPIViews(APITestCase):

    def setUp(self):
        self.book1 = BookInfo.objects.create(
            title='Hobbit',
            publishedDate='1986',
            pageCount='123',
            imageLinks='whatever',
            language='en',
        )
        self.author1 = Authors.objects.create(
            name='J.R.R. Tolkien',
            book=self.book1
        )
        self.isbn1 = Identyfires.objects.create(
            type='ISBN-13',
            identifier='123456754123X',
            book=self.book1
        )

    def test_get_list(self):
        data = {}
        url = api_reverse('apibooklist')
        response = self.client.get(url, data, format= 'json')

        self.assertEquals(response.status_code,200)
        self.assertEquals(response.status_code, status.HTTP_200_OK)